from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from checkout.forms import OrderForm
from owner.models import PostageSettings, Voucher

# Create your views here.
class CheckoutView(generic.ListView):
    
    template_name = "checkout/checkout.html"
    
    def get(self, request, *args, **kwargs):
        # Starting points
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        order_form = OrderForm()
        subtotal = request.session.get('subtotal', 0)
        standard_delivery_cost = round((float(postage_settings.standard_delivery) * subtotal / 100), 2)
        express_delivery_cost = round((float(postage_settings.express_delivery) * subtotal / 100), 2)
        total = subtotal + standard_delivery_cost
        voucher_used = False
        # If User is logged in
        if request.user.is_authenticated:
            order_form = OrderForm(instance=request.user)
        return render(
            request,
            self.template_name,
            {
                "order_form": order_form,
                "standard_delivery_cost": standard_delivery_cost,
                "express_delivery_cost": express_delivery_cost,
                "voucher_used": voucher_used,
                "total": total,
            }
        )
        
    def post(self, request, *args, **kwargs):
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        order_form = OrderForm(request.POST)
        subtotal = request.session.get('subtotal', 0)
        # Delivery starting points
        standard_delivery_cost = round((float(postage_settings.standard_delivery) * subtotal / 100), 2)
        express_delivery_cost = round((float(postage_settings.express_delivery) * subtotal / 100), 2)
        total = subtotal + standard_delivery_cost
        # Vouchers starting points
        voucher_used = False
        usable_voucher = 0
        discount_applied = 0
        if 'check-voucher' in request.POST:
            voucher_code = request.POST.get('voucher')
            if voucher_code != '':
                usable_voucher = Voucher.objects.filter(voucher_code__contains=voucher_code).first()
                if usable_voucher:
                    if usable_voucher.status == 'Active':
                        voucher_used = True
                        discount_applied = round((subtotal * usable_voucher.discount / 100), 2)
                        subtotal = subtotal - discount_applied
                        total = subtotal + standard_delivery_cost
                        messages.success(request, f'Code {usable_voucher.voucher_code} valid. You gained {usable_voucher.discount} % discount.')
                    else:
                        messages.error(request, f"Voucher Code {voucher_code} is not active.")
                        order_form = OrderForm(initial={'voucher': ''})
                else:
                    messages.error(request, f"Voucher Code {voucher_code} is not valid.")
                    order_form = OrderForm(initial={'voucher': ''})
            else:
                messages.error(request, "Voucher Code can't be empty.")
                order_form = OrderForm(initial={'voucher': ''})
        if 'delete-voucher' in request.POST:
            voucher_used = False
            messages.success(request, 'Voucher removed.')
        return render(
            request,
            self.template_name,
            {
                "order_form": order_form,
                "standard_delivery_cost": standard_delivery_cost,
                "express_delivery_cost": express_delivery_cost,
                "voucher_used": voucher_used,
                "usable_voucher": usable_voucher,
                "total": total,
                "discount_applied": discount_applied,
            }
        )