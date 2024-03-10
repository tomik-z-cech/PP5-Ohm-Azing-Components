# PEP8
# Imports
import os
import uuid
import ast
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
    """
    Class starts methods based on webhook type
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        If a webhook that we are not goint to handle received
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_success(self, event):
        """
        If success webhook received
        """
        # Set this variable as the order doesn't exist
        order_exists = False
        # Get data from stripe webhook metadata
        intent = event.data.object
        pid = intent.id
        vault = intent.metadata.vault
        save_details = intent.metadata.save_info
        username = intent.metadata.username
        delivery_option = intent.metadata.delivery_option
        current_voucher = intent.metadata.current_voucher
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        total = round((stripe_charge.amount / 100), 2)
        # Create list of lists from string passed from stripe
        final_vault = ast.literal_eval(vault)
        # Create a subtotal amount from string passed from stripe
        subtotal = round(float(intent.metadata.subtotal), 2)
        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        # Set attempt to 1
        attempt = 1
        # Do this for attempt seconds
        while attempt <= 10:
            try:
                # If order with the same pid exists
                order = Order.objects.get(
                    stripe_pid__startswith=pid,
                )
                # Set order exists
                order_exists = True
                break
            # Order not exist
            except Order.DoesNotExist:
                # Increase attempt counter
                attempt += 1
                # Wait  second
                time.sleep(1)
        # If order already exists
        if order_exists:
            # Return 200 http response
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | \
                    SUCCESS: Verified order already in database',
                status=200,
            )
        # Order received by webhook doesn't exist in the database
        else:
            # If save details check box is on and user loged in
            if save_details and username != "AnonymousUser":
                # Get users profile
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
            # Pre-set VAT to 0
            vat = 0
            # Loop through final vault
            for final_item in final_vault:
                # Get final item in final vault
                current_final_item = get_object_or_404(
                    Item, pk=int(final_item[0])
                )
                # Based on item settings, get the VAT option
                if current_final_item.item_vat_rate == 0:
                    vat_percentage = 1.23
                elif current_final_item.item_vat_rate == 1:
                    vat_percentage = 1.135
                elif current_final_item.item_vat_rate == 2:
                    vat_percentage = 1.09
                else:
                    vat_percentage = 1
                # Check if size is a number
                # (ie package size or size of different form)
                # Not number
                if not str(final_item[1]).isdigit():
                    # Set size multiplier to 1
                    size_multiplier = 1
                # Number
                else:
                    # Get size multiplier from vault
                    size_multiplier = int(final_item[1])
                # Count VAT for current line
                line_vat = round(
                    (
                        int(final_item[3])
                        * size_multiplier
                        * (
                            float(current_final_item.price_per_unit)
                            - (
                                float(current_final_item.price_per_unit)
                                / vat_percentage
                            )
                        )
                    ),
                    2,
                )
                # Update total VAT for the order
                vat = vat + line_vat
            # Get postage settings
            postage_settings = PostageSettings.objects.filter(pk=1).first()
            # Count postage cost
            if subtotal < postage_settings.free_postage:
                standard_delivery_cost = round(
                    (
                        float(postage_settings.standard_delivery)
                        * subtotal
                        / 100
                    ),
                    2,
                )
            else:
                standard_delivery_cost = 0
            express_delivery_cost = round(
                (float(postage_settings.express_delivery) * subtotal / 100), 2
            )
            if delivery_option == "1":
                selected_delivery_cost = express_delivery_cost
            else:
                selected_delivery_cost = standard_delivery_cost
            # Split name from stripe billing details at last space " "
            first_name, last_name = billing_details.name.rsplit(" ", 1)
            # Create new instance of order
            n_o = Order()
            n_o.order_number = uuid.uuid4().hex.upper()
            n_o.user = profile.user
            n_o.delivery_option = delivery_option
            n_o.delivery_cost = selected_delivery_cost
            n_o.sub_total = subtotal
            n_o.vat = vat
            n_o.voucher = current_voucher
            n_o.total = total
            n_o.stripe_pid = pid
            n_o.original_vault = final_vault
            n_o.first_name = first_name
            n_o.last_name = last_name
            n_o.email = billing_details.email
            n_o.phone_number = shipping_details.phone
            n_o.address_1 = shipping_details.address.line1
            n_o.address_2 = shipping_details.address.line2
            n_o.city = shipping_details.address.city
            n_o.county = shipping_details.address.state
            n_o.post_code = shipping_details.address.postal_code
            n_o.country = shipping_details.address.country
            # Generate pdf invoice
            output_filename = f"invoice-{n_o.order_number[:5]}.pdf"
            output_directory = output_directory = "invoices/"
            output_filepath = os.path.join(output_directory, output_filename)
            pdf_file = default_storage.open(output_filepath, "wb")
            with default_storage.open(output_filepath, "wb") as pdf_file:
                pdf = canvas.Canvas(pdf_file)
                now = datetime.now()
                invoice_date = now.strftime("%d.%m.%Y")
                invoice_time = now.strftime("%H:%M")
                pdf.setFont("Helvetica", 12)
                pdf.drawString(
                    245, 815, f"{invoice_date} - {invoice_time} - WH"
                )
                pdf.setFont("Helvetica-Bold", 12)
                pdf.drawString(240, 795, "Ohm-Azing Components")
                pdf.setFont("Helvetica", 12)
                pdf.drawString(147, 775, f"INVOICE # {n_o.order_number}")
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
                    f"{n_o.first_name} {n_o.last_name}",
                    f"{n_o.address_1}, {n_o.city}, {n_o.country}",
                    f"{n_o.email}, {n_o.phone_number}",
                ]
                x_customer = 330
                y_customer = 750 - 13 * 3
                for line in customer_info:
                    pdf.drawString(x_customer, y_customer, line)
                    y_customer -= 13
                pdf.line(5, 640, 565, 640)
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(10, 625, "Item SKU")
                pdf.drawString(80, 625, "Item Name")
                pdf.drawString(215, 625, "Sizes and Values")
                pdf.drawString(360, 625, "Unit Price")
                pdf.drawString(420, 625, "Quantity")
                pdf.drawString(480, 625, "Price")
                y_anchor = 600
                for line in final_vault:
                    pdf.setFont("Helvetica-Bold", 8)
                    invoice_line_item = get_object_or_404(Item, pk=line[0])
                    pdf.drawString(10, y_anchor, invoice_line_item.item_sku)
                    pdf.drawString(80, y_anchor, invoice_line_item.item_name)
                    pdf.setFont("Helvetica", 8)
                    if not line[1] == 1:
                        pdf.drawString(
                            215,
                            y_anchor,
                            f"Size : {line[1]} units - Value : {line[2]}",
                        )
                    pdf.drawString(
                        360,
                        y_anchor,
                        f"{round((invoice_line_item.price_per_unit), 2) \
                            * int(line[1])} €",
                    )
                    pdf.drawString(420, y_anchor, f"{line[3]}")
                    pdf.drawString(
                        480,
                        y_anchor,
                        f"{round((invoice_line_item.price_per_unit), 2) \
                            * int(line[1]) * int(line[3])} €",
                    )
                    y_anchor -= 13
                pdf.line(5, y_anchor, 565, y_anchor)
                y_anchor -= 18
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(290, y_anchor, "Subtotal (excluding VAT) :")
                pdf.setFont("Helvetica", 10)
                pdf.drawString(
                    470, y_anchor, f"{round((subtotal - vat), 2)} €"
                )
                y_anchor -= 18
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(290, y_anchor, "VAT :")
                pdf.setFont("Helvetica", 10)
                pdf.drawString(470, y_anchor, f"{round(vat, 2)} €")
                y_anchor -= 18
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(290, y_anchor, "Subtotal (including VAT) :")
                pdf.setFont("Helvetica", 10)
                pdf.drawString(470, y_anchor, f"{round(subtotal, 2)} €")
                y_anchor -= 18
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(290, y_anchor, "Delivery :")
                pdf.setFont("Helvetica", 10)
                pdf.drawString(
                    470, y_anchor, f"{round(selected_delivery_cost, 2)} €"
                )
                y_anchor -= 18
                pdf.setFont("Helvetica-Bold", 10)
                pdf.drawString(290, y_anchor, "Total :")
                pdf.setFont("Helvetica", 10)
                pdf.drawString(470, y_anchor, f"{round(total, 2)} €")
                y_anchor -= 35
                pdf.line(5, y_anchor, 565, y_anchor)
                pdf.setFont("Helvetica-Bold", 12)
                y_anchor -= 18
                pdf.drawString(200, y_anchor, "THANK YOU FOR YOUR BUSINESS")
                y_anchor -= 18
                pdf.line(5, y_anchor, 565, y_anchor)
                pdf.showPage()
                pdf.save()
            # Save order form
            with default_storage.open(output_filepath, "rb") as pdf_file:
                n_o.invoice.save(output_filename, pdf_file, save=False)
            n_o.save()
            # Send the email to shop for confirmation
            recipient = ["ohmazingcomponents@gmail.com"]
            # Add email of user creating booking
            recipient.append(billing_details.email)
            subject = "New Order at Ohm-Azing Components"
            from_address = "ohmazingcomponents@gmail.com"
            # Count dates for email delivery dates
            if n_o.delivery_option == "0":
                expected_1 = now + timedelta(days=3)
                expected_2 = now + timedelta(days=5)
            elif n_o.delivery_option == "1":
                expected_1 = now + timedelta(days=2)
                expected_2 = now + timedelta(days=3)
            else:
                expected_1 = now + timedelta(days=3)
                expected_2 = now + timedelta(days=5)
            # Generate HTML message from context
            html_message = render_to_string(
                "emails/new_order_template.html",
                {
                    "user": intent.metadata.username,
                    "order_number": n_o.order_number,
                    "expected_1": expected_1.strftime("%d.%m.%Y"),
                    "expected_2": expected_2.strftime("%d.%m.%Y"),
                },
            )
            # Construct an email
            email = EmailMessage(
                subject,
                html_message,
                from_address,
                recipient,
            )
            # Set email type to HTML
            email.content_subtype = "html"
            # Attach PDF file to email
            pdf_file_field = n_o.invoice
            pdf_filename = os.path.basename(pdf_file_field.name)
            pdf_data = pdf_file_field.read()
            email.attach(pdf_filename, pdf_data, "application/pdf")
            # Send email
            email.send()
            # Update stock
            for final_item in final_vault:
                current_final_item = get_object_or_404(Item, pk=final_item[0])
                current_final_item.item_stock = (
                    current_final_item.item_stock - int(final_item[3])
                )
                current_final_item.save()
            # Return 200 http response
            return HttpResponse(
                content=f'Order not in database - created : {event["type"]}',
                status=200,
            )

    def handle_payment_failed(self, event):
        """
        If payment did not succeed
        """
        # Return 200 http response
        return HttpResponse(
            content=f'Payment failed : {event["type"]}', status=200
        )
