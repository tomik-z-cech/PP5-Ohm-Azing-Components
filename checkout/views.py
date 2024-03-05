import json
import stripe
from decimal import Decimal
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.conf import settings
from checkout.forms import OrderForm
from owner.models import PostageSettings, Voucher
from items.models import Item

# Create your views here.
class CheckoutView(generic.ListView):
    
    template_name = "checkout/checkout.html"
    success_name = "checkout/checkout_ok.html"
    
    def get(self, request, *args, **kwargs):
        # Starting points
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        order_form = OrderForm()
        subtotal = request.session.get('subtotal', 0)
        if subtotal == 0:
            messages.error(request, "Can't proceed to checkout with empty Vault")
            return redirect('shop', category_pk = 0)
        elif subtotal < postage_settings.minimum_order:
            messages.error(request, f"Can't proceed to checkout. The minimum order value is {postage_settings.minimum_order} €.")
            return redirect('shop', category_pk = 0)
        else:
            if subtotal < postage_settings.free_postage:
                standard_delivery_cost = round((float(postage_settings.standard_delivery) * subtotal / 100), 2)
            else:
                standard_delivery_cost = 0
            express_delivery_cost = round((float(postage_settings.express_delivery) * subtotal / 100), 2)
            voucher_used = False
            # If User is logged in
            if request.user.is_authenticated:
                order_form = OrderForm(instance=request.user.userprofile)
            # Total    
            total = round((subtotal + standard_delivery_cost), 2)
            # Stripe
            stripe_public_key = settings.STRIPE_PUBLIC_KEY
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe_total = int(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount = stripe_total,
                currency = settings.STRIPE_CURRENCY
            )
            if not stripe_public_key:
                messages.error(request, 'Stripe public key missing.')
            return render(
                request,
                self.template_name,
                {
                    "order_form": order_form,
                    "standard_delivery_cost": standard_delivery_cost,
                    "express_delivery_cost": express_delivery_cost,
                    "voucher_used": voucher_used,
                    "total": total,
                    "stripe_public_key": stripe_public_key,
                    "client_secret": intent.client_secret,
                }
            )
        
    def post(self, request, *args, **kwargs):
        """
        Voucher in use : voucher_used, voucher_code, discount_applied, voucher_discount
        """
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        order_form = OrderForm(request.POST)
        subtotal = request.session.get('subtotal', 0)
        if subtotal == 0:
            messages.error(request, "Can't proceed to checkout with empty Vault")
            return redirect('shop', category_pk = 0)
        else:
            # Delivery starting points
            if subtotal < postage_settings.free_postage:
                standard_delivery_cost = round((float(postage_settings.standard_delivery) * subtotal / 100), 2)
            else:
                standard_delivery_cost = 0
            express_delivery_cost = round((float(postage_settings.express_delivery) * subtotal / 100), 2)
            # Vouchers starting points
            current_voucher = request.session.get('current_voucher', [False, '', 0, 0])
            if 'delivery' in request.POST:
                if request.POST.get('delivery_option') == '1':
                    selected_delivery_cost = express_delivery_cost
                    request.session['selected_delivery'] = '1'
                else:
                    selected_delivery_cost = standard_delivery_cost
                    request.session['selected_delivery'] = '0'
            if request.POST.get('delivery_option') == '1':
                selected_delivery_cost = express_delivery_cost
                request.session['selected_delivery'] = '1'
            else:
                selected_delivery_cost = standard_delivery_cost
                request.session['selected_delivery'] = '0'
            if 'check-voucher' in request.POST:
                voucher_code = request.POST.get('voucher','')
                if voucher_code != '':
                    usable_voucher = Voucher.objects.filter(voucher_code__contains=voucher_code).first()
                    if usable_voucher:
                        current_voucher[1] = usable_voucher.voucher_code
                        if usable_voucher.status == 'Active':
                            current_voucher[0] = True
                            current_voucher[2] = round((subtotal * usable_voucher.discount / 100), 2)
                            current_voucher[3] = usable_voucher.discount
                            subtotal = subtotal - current_voucher[2]
                            messages.success(request, f'Code {usable_voucher.voucher_code} valid. You gained {usable_voucher.discount} % discount.')
                        else:
                            messages.error(request, f"Voucher Code {voucher_code} is not active.")
                    else:
                        messages.error(request, f"Voucher Code {voucher_code} is not valid.")
                else:
                    messages.error(request, "Voucher Code can't be empty.")
            request.session['current_voucher'] = current_voucher
            if 'delete-voucher' in request.POST:
                current_voucher = [False, '', 0, 0]
                messages.success(request, 'Voucher removed.')
                request.session['current_voucher'] = current_voucher
            # Total
            total = round((subtotal + selected_delivery_cost), 2)
            # Stripe
            stripe_public_key = settings.STRIPE_PUBLIC_KEY
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe_total = int(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount = stripe_total,
                currency = settings.STRIPE_CURRENCY
            )
            if not stripe_public_key:
                messages.error(request, 'Stripe public key missing.')
            if request.POST.get('payment-checker') == 'true' and order_form.is_valid():
                # If save details check box is on and user loged in 
                if 'save-details' in request.POST and request.user.is_authenticated:
                    # Save all details provided by user
                    logged_userprofile = request.user.userprofile
                    logged_userprofile.first_name = order_form.cleaned_data['first_name']
                    logged_userprofile.last_name = order_form.cleaned_data['last_name']
                    logged_userprofile.phone_number = order_form.cleaned_data['phone_number']
                    logged_userprofile.address_1 = order_form.cleaned_data['address_1']
                    logged_userprofile.address_2 = order_form.cleaned_data['address_2']
                    logged_userprofile.city = order_form.cleaned_data['city']
                    logged_userprofile.county = order_form.cleaned_data['county']
                    logged_userprofile.post_code = order_form.cleaned_data['post_code']
                    logged_userprofile.country = order_form.cleaned_data['country']
                    logged_userprofile.save()
                # VAT counter
                final_vault = request.session.get('vault','')
                vat = 0
                for final_item in final_vault:
                    current_final_item = get_object_or_404(Item,pk=final_item[0])
                    if current_final_item.item_vat_rate == 0:
                        vat_percentage = 1.23
                    elif current_final_item.item_vat_rate == 1:
                        vat_percentage = 1.135
                    elif current_final_item.item_vat_rate == 2:
                        vat_percentage = 1.09
                    else:
                        vat_percentage = 1
                    # Check if size is a digit (ie package size or size of different form)
                    if not str(final_item[1]).isdigit():
                        print('not digit')
                        size_multiplier = 1
                    else:
                        size_multiplier = int(final_item[1])
                    line_vat = round((int(final_item[3]) * size_multiplier * (float(current_final_item.price_per_unit) - (float(current_final_item.price_per_unit) / vat_percentage ))), 2)
                    vat = vat + line_vat
                # Create new instance of order
                new_order = order_form.save(commit=False)
                new_order.user = request.user
                new_order.delivery_option = request.POST.get('delivery_option')
                new_order.delivery_cost = selected_delivery_cost
                new_order.sub_total = subtotal
                new_order.vat = vat
                new_order.voucher = current_voucher
                new_order.total = total
                new_order.stripe_pid = request.POST.get('client_secret')
                new_order.original_vault = json.dumps(final_vault)
                # Save order form
                new_order.save()
                # Reset any voucher in use
                current_voucher = [False, '', 0, 0]
                request.session['current_voucher'] = current_voucher
                return render(
                request,
                self.success_name,
                )
            else:
                messages.error(request, 'There was an error with your order. Please double check your information.')
            return render(
                request,
                self.template_name,
                {
                    "order_form": order_form,
                    "standard_delivery_cost": standard_delivery_cost,
                    "express_delivery_cost": express_delivery_cost,
                    "current_voucher": current_voucher,
                    "total": total,
                    "selected_delivery_cost": selected_delivery_cost,
                    "stripe_public_key": stripe_public_key,
                    "client_secret": intent.client_secret,
                }
            )
        
class CheckCheckoutDataView(generic.ListView):
    def post(self, request, *args, **kwargs):
        try:
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(pid, metadata={
                'vault': json.dumps(request.session.get('vault', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
            })
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, "Sorry, we can't process your payment right now. Please try again later.")
            return HttpResponse(content=e, status=400)
