# Imports
import os
import json
import uuid
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
import stripe
from checkout.forms import OrderForm
from owner.models import PostageSettings, Voucher
from items.models import Item


# Create your views here.
class CheckoutView(generic.ListView):
    
    template_name = "checkout/checkout.html"
    
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
                # VAT counter + PDF dictionary creator
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
                        size_multiplier = 1
                    else:
                        size_multiplier = int(final_item[1])
                    line_vat = round((int(final_item[3]) * size_multiplier * (float(current_final_item.price_per_unit) - (float(current_final_item.price_per_unit) / vat_percentage ))), 2)
                    vat = vat + line_vat
                # Create new instance of order
                new_order = order_form.save(commit=False)
                new_order.order_number = uuid.uuid4().hex.upper()
                new_order.user = request.user
                new_order.delivery_option = request.POST.get('delivery_option')
                new_order.delivery_cost = selected_delivery_cost
                new_order.sub_total = subtotal
                new_order.vat = vat
                new_order.voucher = current_voucher
                new_order.total = total
                new_order.stripe_pid = request.POST.get('client_secret')
                new_order.original_vault = json.dumps(final_vault)
                # Generate pdf invoice
                output_filename = f'invoice-{new_order.order_number[:5]}.pdf'
                output_directory = output_directory = 'invoices/'
                output_filepath = os.path.join(output_directory, output_filename)
                pdf_file = default_storage.open(output_filepath, 'wb')
                with default_storage.open(output_filepath, 'wb') as pdf_file:   
                    pdf = canvas.Canvas(pdf_file)
                    today_date = datetime.today()
                    invoice_date = today_date.strftime('%d.%m.%Y')
                    pdf.setFont("Helvetica", 12)
                    pdf.drawString(270,815, f'{invoice_date}')
                    pdf.setFont("Helvetica-Bold", 12)
                    pdf.drawString(240, 795, 'Ohm-Azing Components')
                    pdf.setFont("Helvetica", 12)
                    pdf.drawString(147, 775, f'INVOICE # {new_order.order_number}')
                    pdf.line(5, 760, 565, 760)
                    seller_info = [
                        "Ohm-Azing Components",
                        "Borrisokane, Co. Tipperary, ",
                        "ohmazingcomponents@gmail.com",
                    ]
                    y_seller = 750 - 13 * 3
                    pdf.setFont("Helvetica-Bold", 12)
                    for line in seller_info:
                        pdf.drawString(20, y_seller, line)
                        y_seller -= 13
                    customer_info = [
                        f"{new_order.first_name} {new_order.last_name}",
                        f"{new_order.address_1}, {new_order.city}, {new_order.country}",
                        f"{new_order.email}, {new_order.phone_number}",
                    ]
                    x_customer = 330
                    y_customer = 750 - 13 * 3
                    for line in customer_info:
                        pdf.drawString(x_customer, y_customer, line)
                        y_customer -= 13
                    pdf.line(5, 640, 565, 640)
                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(10, 625, 'Item SKU')
                    pdf.drawString(80, 625, 'Item Name')
                    pdf.drawString(215, 625, 'Sizes and Values')
                    pdf.drawString(360, 625, 'Unit Price')
                    pdf.drawString(420, 625, 'Quantity')
                    pdf.drawString(480, 625, 'Price')
                    y_anchor = 600
                    for line in final_vault:
                        pdf.setFont("Helvetica-Bold", 8)
                        invoice_line_item = get_object_or_404(Item, pk=line[0])
                        pdf.drawString(10, y_anchor, invoice_line_item.item_sku)
                        pdf.drawString(80, y_anchor, invoice_line_item.item_name)
                        pdf.setFont("Helvetica", 8)
                        if not line[1] == 1:
                            pdf.drawString(215, y_anchor, f'Size : {line[1]} units - Value : {line[2]}')
                        pdf.drawString(360, y_anchor, f'{round((invoice_line_item.price_per_unit), 2) * int(line[1])} €')
                        pdf.drawString(420, y_anchor, f'{line[3]}')
                        pdf.drawString(480, y_anchor, f'{round((invoice_line_item.price_per_unit), 2) * int(line[1]) * int(line[3])} €')
                        y_anchor -= 13
                    pdf.line(5, y_anchor, 565, y_anchor)
                    y_anchor -= 18
                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(290, y_anchor, 'Subtotal (excluding VAT) :')
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(470, y_anchor, f'{subtotal - vat} €')
                    y_anchor -= 18
                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(290, y_anchor, 'VAT :')
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(470, y_anchor, f'{vat} €')
                    y_anchor -= 18
                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(290, y_anchor, 'Subtotal(including VAT) :')
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(470, y_anchor, f'{subtotal} €')
                    y_anchor -= 18
                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(290, y_anchor, 'Delivery :')
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(470, y_anchor, f'{selected_delivery_cost} €')
                    y_anchor -= 18
                    pdf.setFont("Helvetica-Bold", 10)
                    pdf.drawString(290, y_anchor, 'Total :')
                    pdf.setFont("Helvetica", 10)
                    pdf.drawString(470, y_anchor, f'{total} €')
                    y_anchor -= 35
                    pdf.line(5, y_anchor, 565, y_anchor)
                    pdf.setFont("Helvetica-Bold", 12)
                    y_anchor -= 18
                    pdf.drawString(200, y_anchor, 'THANK YOU FOR YOUR BUSINESS')
                    y_anchor -= 18
                    pdf.line(5, y_anchor, 565, y_anchor)
                    pdf.showPage()
                    pdf.save()
                # Save order form
                with default_storage.open(output_filepath, 'rb') as pdf_file:
                    new_order.invoice.save(output_filename, pdf_file, save=False)
                new_order.save()
                # Prefixes for confirmation email
                recipient = [
                    "ohmazingcomponents@gmail.com"
                ]  # Send the email to myself as confirmation
                # Add email of user creating booking
                recipient.append(request.user.email)
                subject = "New Order at Ohm-Azing Components"  # Subject
                from_address = "ohmazingcomponents@gmail.com"  # From
                if new_order.delivery_option == '0':
                    expected_1 = today_date + timedelta(days=3)
                    expected_2 = today_date + timedelta(days=5)
                elif new_order.delivery_option == '1':
                    expected_1 = today_date + timedelta(days=2)
                    expected_2 = today_date + timedelta(days=3)
                else:
                    expected_1 = today_date + timedelta(days=3)
                    expected_2 = today_date + timedelta(days=5)
                html_message = render_to_string("emails/new_order_template.html",{
                    "user": request.user.username,
                    "order_number": new_order.order_number,
                    "expected_1": expected_1.strftime('%d.%m.%Y'),
                    "expected_2": expected_2.strftime('%d.%m.%Y'),
                    })
                email = EmailMessage(
                    subject,
                    html_message,
                    from_address,
                    recipient,
                )
                email.content_subtype = 'html'
                pdf_file_field = new_order.invoice
                pdf_filename = os.path.basename(pdf_file_field.name)
                pdf_data = pdf_file_field.read()
                email.attach(pdf_filename, pdf_data, 'application/pdf')
                email.send()
                # Reset any voucher in use
                current_voucher = [False, '', 0, 0]
                request.session['current_voucher'] = current_voucher
                # Update stock
                for final_item in final_vault:
                    current_final_item = get_object_or_404(Item,pk=final_item[0])
                    current_final_item.item_stock = current_final_item.item_stock - int(final_item[3])
                    current_final_item.save()
                messages.success(request, f'Your order {new_order.order_number} was successfully created.')
                return redirect('order-success', order_number=new_order.order_number, delivery_option=new_order.delivery_option)
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
                'delivery_option': request.POST.get('delivery-option'),
                'subtotal': request.POST.get('subtotal'),
                'current_voucher': request.POST.get('current-voucher'),
            })
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, "Sorry, we can't process your payment right now. Please try again later.")
            return HttpResponse(content=e, status=400)
        
class OrderSuccessView(generic.ListView):
    
    template_name = "checkout/checkout_ok.html"
    
    def get(self, request, order_number, delivery_option, *args, **kwargs):
        today_date = datetime.today()
        if delivery_option == '0':
            expected_1 = today_date + timedelta(days=3)
            expected_2 = today_date + timedelta(days=5)
        elif delivery_option == '1':
            expected_1 = today_date + timedelta(days=2)
            expected_2 = today_date + timedelta(days=3)
        else:
            expected_1 = today_date + timedelta(days=3)
            expected_2 = today_date + timedelta(days=5)
        success_vault = request.session.get('vault',[])
        translated_vault_content = []
        # For each item in Vault
        for vault_item in success_vault:
            # Get item from database
            item_per_line = get_object_or_404(Item, pk=vault_item[0])
            # Add price of each item to Subtotal
            price_per_line = item_per_line.price_per_unit * int(vault_item[1]) * int(vault_item[3])
            # Translate each record in vault for template
            translated_vault_item = [vault_item[0],vault_item[1],vault_item[2],vault_item[3], item_per_line.item_name, item_per_line.image_1, item_per_line.price_per_unit, item_per_line.item_stock, price_per_line]
            translated_vault_content.append(translated_vault_item)
        print(translated_vault_content)
        return render(
                request,
                self.template_name,
                {
                    "order_number": order_number,
                    "expected_1": expected_1,
                    "expected_2": expected_2,
                    "success_vault": translated_vault_content,
                }
            )