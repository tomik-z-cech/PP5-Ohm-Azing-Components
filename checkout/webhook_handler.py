import os
import uuid
import time
from django.shortcuts import HttpResponse, get_object_or_404
from django.core.files.storage import default_storage
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import stripe
from .models import Order
from profilemanager.models import UserProfile
from items.models import Item
from owner.models import PostageSettings

class StripeWH_Handler:
    
    def __init__(self, request):
        self.request = request
        
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
        
    def handle_payment_success(self,event):
        print('got webhook')
        intent = event.data.object
        pid = intent.id
        vault = intent.metadata.vault
        save_details = intent.metadata.save_info
        username = intent.metadata.username
        delivery_option = intent.metadata.delivery_option
        subtotal = intent.metadata.subtotal
        current_voucher = intent.metadata.current_voucher
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        total = round((stripe_charge.amount / 100), 2)
        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        attempt = 1
        while attempt <= 15:
            try:
                order = Order.objects.get(
                        email__iexact=billing_details.email,
                        phone_number__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        post_code__iexact=shipping_details.address.postal_code,
                        city__iexact=shipping_details.address.city,
                        address_1__iexact=shipping_details.address.line1,
                        county__iexact=shipping_details.address.state,
                        total=total,
                        original_vault=vault,
                        stripe_pid=pid,
                    )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            # If save details check box is on and user loged in 
            if save_details and username != 'AnonymousUser':
                profile = UserProfile.objects.get(user__username=username)
                # Save all details provided by user
                profile.phone_number = shipping_details.phone
                profile.country = shipping_details.address.country
                profile.post_code = shipping_details.address.postal_code
                profile.city = shipping_details.address.city
                profile.address_1 = shipping_details.address.line1
                profile.address_2 = shipping_details.address.line2
                profile.county = shipping_details.address.state
                profile.save()
            # VAT counter + PDF dictionary creator
            final_vault = vault
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
            postage_settings = PostageSettings.objects.filter(pk=1).first()
            if subtotal < postage_settings.free_postage:
                standard_delivery_cost = round((float(postage_settings.standard_delivery) * subtotal / 100), 2)
            else:
                standard_delivery_cost = 0
            express_delivery_cost = round((float(postage_settings.express_delivery) * subtotal / 100), 2)
            if delivery_option == '1':
                selected_delivery_cost = express_delivery_cost
            else:
                selected_delivery_cost = standard_delivery_cost
            # Create new instance of order
            new_order = Order.objects.create()
            new_order.order_number = uuid.uuid4().hex.upper()
            new_order.user = username
            new_order.delivery_option = delivery_option
            new_order.delivery_cost = selected_delivery_cost
            new_order.sub_total = subtotal
            new_order.vat = vat
            new_order.voucher = current_voucher
            new_order.total = total
            new_order.stripe_pid = pid
            new_order.original_vault = final_vault
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
            recipient.append(billing_details.email)
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
                "user": intent.metadata.username,
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
            # Update stock
            for final_item in final_vault:
                current_final_item = get_object_or_404(Item,pk=final_item[0])
                current_final_item.item_stock = current_final_item.item_stock - int(final_item[3])
                current_final_item.save()
            return HttpResponse(
                content=f"Order wasn't in database - created : {event["type"]}",
                status=200)
        
    def handle_payment_failed(self,event):
        return HttpResponse(
            content=f'Payment failed : {event["type"]}',
            status=200)