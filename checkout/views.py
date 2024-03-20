# PEP8
# Imports
import os
import json
import uuid
import copy
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
    """
    Class creates view for checkout
    """

    template_name = "checkout/checkout.html"

    def get(self, request, *args, **kwargs):
        """
        Method creates view for chceckout
        """
        # Postage settings field
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        # Order form
        order_form = OrderForm()
        # Get subtotal from session - default 0
        subtotal = request.session.get("subtotal", 0)
        # Current voucher in use
        current_voucher = [False, "", 0, 0]
        # If subtotal equals to 0 (empty vault)
        if subtotal == 0:
            messages.error(
                request, "Can't proceed to checkout with empty Vault"
            )
            # Redirect back to shop
            return redirect("shop", category_pk=0)
        # Or subtotal is less than minimum order
        elif subtotal < postage_settings.minimum_order:
            messages.error(
                request,
                f"Can't proceed to checkout. \
                    The minimum order value \
                    is {postage_settings.minimum_order} €.",
            )
            # Redirect back to shop
            return redirect("shop", category_pk=0)
        # Vault not empty and bigger than minimum order amount
        else:
            # If subtotal less than free postage treshold
            if subtotal < postage_settings.free_postage:
                # Count cost of standard delivery cost
                standard_delivery_cost = round(
                    (
                        float(postage_settings.standard_delivery)
                        * subtotal
                        / 100
                    ),
                    2,
                )
            # Subtotal more than free postage treshold
            else:
                # Cost of standard delivery is 0 (free delivery)
                standard_delivery_cost = 0
            # Count cost of express delivery cost
            express_delivery_cost = round(
                (float(postage_settings.express_delivery) * subtotal / 100), 2
            )
            # Voucher in use - false
            voucher_used = False
            # If User is logged in
            if request.user.is_authenticated:
                # Prefill order form with save shipping details
                order_form = OrderForm(instance=request.user.userprofile)
            # Count total cost
            total = round((subtotal + standard_delivery_cost), 2)
            # Stripe settings and creation of payment intent
            stripe_public_key = settings.STRIPE_PUBLIC_KEY
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe_total = int(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total, currency=settings.STRIPE_CURRENCY
            )
            # In case of public key missing
            if not stripe_public_key:
                messages.error(request, "Stripe public key missing.")
            # Render checkout template
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
                    "subtotal": subtotal,
                    "current_voucher": current_voucher,
                },
            )

    def post(self, request, *args, **kwargs):
        """
        Method is called when user changes voucher,
        delivery option or payment submitted
        Voucher in use : voucher_used, voucher_code,
        discount_applied, voucher_discount
        """
        # Get postage settings
        postage_settings = PostageSettings.objects.filter(pk=1).first()
        # Get order form from request.POST
        order_form = OrderForm(request.POST)
        # Get subtotal from session
        subtotal = request.session.get("subtotal", 0)
        # If subtotal equals 0 (empty vault)
        if subtotal == 0:
            messages.error(
                request, "Can't proceed to checkout with empty Vault"
            )
            # Redirect back to shop
            return redirect("shop", category_pk=0)
        # If subtotal less than minimum order amount
        elif subtotal < postage_settings.minimum_order:
            messages.error(
                request,
                f"Can't proceed to checkout.\
                    The minimum order value is \
                    {postage_settings.minimum_order} €.",
            )
            # Redirect back to shop
            return redirect("shop", category_pk=0)
        # Vault not empty and bigger than minimum order amount
        else:
            # If subtotal less than free delivery treshold
            if subtotal < postage_settings.free_postage:
                # Count standard delivery cost
                standard_delivery_cost = round(
                    (
                        float(postage_settings.standard_delivery)
                        * subtotal
                        / 100
                    ),
                    2,
                )
            # Subtotal greater than free delivery treshold
            else:
                # Standard delivery cost = 0 (FREE delivery)
                standard_delivery_cost = 0
            # Count cost of express delivery
            express_delivery_cost = round(
                (float(postage_settings.express_delivery) * subtotal / 100), 2
            )
            # Request current voucher from session
            current_voucher = request.session.get(
                "current_voucher", [False, "", 0, 0]
            )
            # If user changes delivery option
            if "delivery" in request.POST:
                # If submitted delivery option equals 1
                if request.POST.get("delivery_option") == "1":
                    # Set selected delivery to express
                    selected_delivery_cost = express_delivery_cost
                    # Set selected delivery into session
                    request.session["selected_delivery"] = "1"
                # Submitted delivery option is not 1
                else:
                    # Set selected delivery as standard
                    selected_delivery_cost = standard_delivery_cost
                    # Set selected delivery into session
                    request.session["selected_delivery"] = "0"
            # Set delivery cost based on request.POST
            # If selected option equals to 1
            if request.POST.get("delivery_option") == "1":
                # Set selected delivery as express
                selected_delivery_cost = express_delivery_cost
                # Save selected option into session
                request.session["selected_delivery"] = "1"
            # Selected delivery option not equal to 1
            else:
                # Set selected delivery as standard
                selected_delivery_cost = standard_delivery_cost
                # Save option into session
                request.session["selected_delivery"] = "0"
            # If users submits voucher code
            if "check-voucher" in request.POST:
                # Get voucher code from request.POST
                voucher_code = request.POST.get("voucher", "")
                # If submitted code not empty string
                if voucher_code != "":
                    # Check database if code exists
                    usable_voucher = Voucher.objects.filter(
                        voucher_code__contains=voucher_code
                    ).first()
                    # If code does exist
                    if usable_voucher:
                        # Set the code into current voucher
                        current_voucher[1] = usable_voucher.voucher_code
                        # If usable voucher is active (based on dates)
                        if usable_voucher.status == "Active":
                            # Set current voucher as being used
                            current_voucher[0] = True
                            # Count applied dicount
                            current_voucher[2] = round(
                                (subtotal * usable_voucher.discount / 100), 2
                            )
                            # Get discount percentage
                            current_voucher[3] = usable_voucher.discount
                            # Recount subtotal based on voucher
                            subtotal = subtotal - current_voucher[2]
                            messages.success(
                                request,
                                f"Code {usable_voucher.voucher_code} valid. \
                                    You gained {usable_voucher.discount} \
                                    % discount.",
                            )
                        # If Voucher not active
                        else:
                            messages.error(
                                request,
                                f"Voucher Code {voucher_code} is not active.",
                            )
                    # Provided code not valid
                    else:
                        messages.error(
                            request,
                            f"Voucher Code {voucher_code} is not valid.",
                        )
                # Submitted empty string
                else:
                    messages.error(request, "Voucher Code can't be empty.")
            # Save current voucher into session
            request.session["current_voucher"] = current_voucher
            # If users requests to delete voucher code already in use
            if "delete-voucher" in request.POST:
                # Set current voucher to empty voucher
                current_voucher = [False, "", 0, 0]
                messages.success(request, "Voucher removed.")
                # Save current voucher to session
                request.session["current_voucher"] = current_voucher
            # Count total
            total = round((subtotal + selected_delivery_cost), 2)
            # Stripe settings and creation of payment intent
            stripe_public_key = settings.STRIPE_PUBLIC_KEY
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe_total = int(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total, currency=settings.STRIPE_CURRENCY
            )
            # In case of public key is missing
            if not stripe_public_key:
                messages.error(request, "Stripe public key missing.")
            # If user submits payment ...
            if request.POST.get("payment-checker") == "true":
                # ... and checkout form is vaild
                if order_form.is_valid():
                    # If save details check box is on and user loged in
                    if (
                        "save-details" in request.POST
                        and request.user.is_authenticated
                    ):
                        # Save all details provided by user
                        logged_userprofile = request.user.userprofile
                        logged_userprofile.first_name = (
                            order_form.cleaned_data["first_name"]
                        )
                        logged_userprofile.last_name = order_form.cleaned_data[
                            "last_name"
                        ]
                        logged_userprofile.phone_number = (
                            order_form.cleaned_data["phone_number"]
                        )
                        logged_userprofile.address_1 = order_form.cleaned_data[
                            "address_1"
                        ]
                        logged_userprofile.address_2 = order_form.cleaned_data[
                            "address_2"
                        ]
                        logged_userprofile.city = order_form.cleaned_data[
                            "city"
                        ]
                        logged_userprofile.county = order_form.cleaned_data[
                            "county"
                        ]
                        logged_userprofile.post_code = order_form.cleaned_data[
                            "post_code"
                        ]
                        logged_userprofile.country = order_form.cleaned_data[
                            "country"
                        ]
                        logged_userprofile.save()
                    # Get final vault from session
                    final_vault = request.session.get("vault", "")
                    # Pre-set VAT to 0
                    vat = 0
                    # Loop through final vault
                    for final_item in final_vault:
                        # Get final item in final vault
                        current_final_item = get_object_or_404(
                            Item, pk=final_item[0]
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
                                        float(
                                            current_final_item.price_per_unit
                                        )
                                        / vat_percentage
                                    )
                                )
                            ),
                            2,
                        )
                        # Update total VAT for the order
                        vat = vat + line_vat
                    # Create new instance of order
                    n_o = order_form.save(commit=False)
                    n_o.order_number = uuid.uuid4().hex.upper()
                    if request.user.is_authenticated:
                        n_o.user = request.user
                    n_o.email = request.POST.get('email')
                    n_o.delivery_option = request.POST.get("delivery_option")
                    n_o.delivery_cost = selected_delivery_cost
                    n_o.sub_total = subtotal
                    n_o.vat = vat
                    n_o.voucher = current_voucher
                    n_o.total = total
                    n_o.stripe_pid = request.POST.get("client_secret")[:27]
                    n_o.original_vault = json.dumps(final_vault)
                    # Generate pdf invoice
                    output_filename = f"invoice-{n_o.order_number[:5]}.pdf"
                    output_directory = output_directory = "invoices/"
                    output_filepath = os.path.join(
                        output_directory, output_filename
                    )
                    pdf_file = default_storage.open(output_filepath, "wb")
                    with default_storage.open(
                        output_filepath, "wb"
                    ) as pdf_file:
                        pdf = canvas.Canvas(pdf_file)
                        now = datetime.now()
                        invoice_date = now.strftime("%d.%m.%Y")
                        invoice_time = now.strftime("%H:%M")
                        pdf.setFont("Helvetica", 12)
                        pdf.drawString(
                            253, 815, f"{invoice_date} - {invoice_time}"
                        )
                        pdf.setFont("Helvetica-Bold", 12)
                        pdf.drawString(240, 795, "Ohm-Azing Components")
                        pdf.setFont("Helvetica", 12)
                        pdf.drawString(
                            147, 775, f"INVOICE # {n_o.order_number}"
                        )
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
                            line_item = get_object_or_404(
                                Item, pk=line[0]
                            )
                            pdf.drawString(
                                10, y_anchor, line_item.item_sku
                            )
                            pdf.drawString(
                                80, y_anchor, line_item.item_name
                            )
                            pdf.setFont("Helvetica", 8)
                            if not line[1] == 1:
                                pdf.drawString(
                                    215,
                                    y_anchor,
                                    f"Size : {line[1]} units - \
                                        Value : {line[2]}",
                                )
                            pdf.drawString(
                                360,
                                y_anchor,
                                f"{round((line_item.price_per_unit), 2) \
                                    * int(line[1])} €",
                            )
                            pdf.drawString(420, y_anchor, f"{line[3]}")
                            pdf.drawString(
                                480,
                                y_anchor,
                                f"{round((line_item.price_per_unit), 2) * \
                                    int(line[1]) * int(line[3])} €",
                            )
                            y_anchor -= 13
                        pdf.line(5, y_anchor, 565, y_anchor)
                        y_anchor -= 18
                        pdf.setFont("Helvetica-Bold", 10)
                        pdf.drawString(
                            290, y_anchor, "Subtotal (excluding VAT) :"
                        )
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
                        pdf.drawString(
                            290, y_anchor, "Subtotal(including VAT) :"
                        )
                        pdf.setFont("Helvetica", 10)
                        pdf.drawString(
                            470, y_anchor, f"{round(subtotal, 2)} €"
                        )
                        y_anchor -= 18
                        pdf.setFont("Helvetica-Bold", 10)
                        pdf.drawString(290, y_anchor, "Delivery :")
                        pdf.setFont("Helvetica", 10)
                        pdf.drawString(
                            470,
                            y_anchor,
                            f"{round(selected_delivery_cost, 2)} €",
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
                        pdf.drawString(
                            200, y_anchor, "THANK YOU FOR YOUR BUSINESS"
                        )
                        y_anchor -= 18
                        pdf.line(5, y_anchor, 565, y_anchor)
                        pdf.showPage()
                        pdf.save()
                    # Save order form
                    with default_storage.open(
                        output_filepath, "rb"
                    ) as pdf_file:
                        n_o.invoice.save(output_filename, pdf_file, save=False)
                    n_o.save()
                    # Send order to the shop for confirmation
                    recipient = ["ohmazingcomponents@gmail.com"]
                    # Add email of user creating booking
                    recipient.append(n_o.email)
                    subject = "New Order at Ohm-Azing Components"
                    from_address = "ohmazingcomponents@gmail.com"
                    # Get dates for email
                    if n_o.delivery_option == "0":
                        expected_1 = now + timedelta(days=3)
                        expected_2 = now + timedelta(days=5)
                    elif n_o.delivery_option == "1":
                        expected_1 = now + timedelta(days=2)
                        expected_2 = now + timedelta(days=3)
                    else:
                        expected_1 = now + timedelta(days=3)
                        expected_2 = now + timedelta(days=5)
                    # HTML message
                    html_message = render_to_string(
                        "emails/new_order_template.html",
                        {
                            "user": request.user.username,
                            "order_number": n_o.order_number,
                            "expected_1": expected_1.strftime("%d.%m.%Y"),
                            "expected_2": expected_2.strftime("%d.%m.%Y"),
                        },
                    )
                    # Construc email
                    email = EmailMessage(
                        subject,
                        html_message,
                        from_address,
                        recipient,
                    )
                    # Set content of email to HTML
                    email.content_subtype = "html"
                    # Get PDF invoice and attach to email
                    pdf_file_field = n_o.invoice
                    pdf_filename = os.path.basename(pdf_file_field.name)
                    pdf_data = pdf_file_field.read()
                    email.attach(pdf_filename, pdf_data, "application/pdf")
                    # Send email
                    email.send()
                    # Reset any voucher in use
                    current_voucher = [False, "", 0, 0]
                    request.session["current_voucher"] = current_voucher
                    # Update stock
                    for final_item in final_vault:
                        current_final_item = get_object_or_404(
                            Item, pk=final_item[0]
                        )
                        current_final_item.item_stock = (
                            current_final_item.item_stock - int(final_item[3])
                        )
                        current_final_item.save()
                    messages.success(
                        request,
                        f"Your order {n_o.order_number} successfully created.",
                    )
                    # Redirect to order succss page
                    return redirect(
                        "order-success",
                        order_number=n_o.order_number,
                        delivery_option=n_o.delivery_option,
                    )
                # Order form not valid
                else:
                    messages.error(
                        request,
                        "There was an error with your order. \
                            Please double check your information.",
                    )
            # User request is not check vocuher,
            # clear voucher or submit payment.
            else:
                messages.success(
                    request, "Delivery option successfully updated."
                )
            # Render checkout template
            return render(
                request,
                self.template_name,
                {
                    "order_form": order_form,
                    "standard_delivery_cost": standard_delivery_cost,
                    "express_delivery_cost": express_delivery_cost,
                    "total": total,
                    "selected_delivery_cost": selected_delivery_cost,
                    "subtotal": subtotal,
                    "current_voucher": current_voucher,
                    "stripe_public_key": stripe_public_key,
                    "client_secret": intent.client_secret,
                },
            )


class CheckCheckoutDataView(generic.ListView):
    """
    Class checks posted data by stripe_elements.js
    """

    def post(self, request, *args, **kwargs):
        """
        Method checks if all data valid
        """
        # Try to gather all data posted by stripe_elements.js
        try:
            pid = request.POST.get("client_secret").split("_secret")[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(
                pid,
                metadata={
                    "vault": json.dumps(request.session.get("vault", {})),
                    "save_info": request.POST.get("save_info"),
                    "username": request.user,
                    "delivery_option": request.POST.get("delivery_option"),
                    "subtotal": request.POST.get("subtotal"),
                    "current_voucher": request.POST.get("current_voucher"),
                },
            )
            # Return succes http response
            return HttpResponse(status=200)
        # If there's problem with the data
        except Exception as e:
            messages.error(
                request,
                "Sorry, we can't process your payment \
                    right now. Please try again later.",
            )
            # Return error http response
            return HttpResponse(content=e, status=400)


class OrderSuccessView(generic.ListView):
    """
    Class renders order success page
    """

    template_name = "checkout/checkout_ok.html"

    def get(self, request, order_number, delivery_option, *args, **kwargs):
        """
        Method renders succes checkout template with order details
        """
        # Get today's date
        today_date = datetime.today()
        # Based on selected deliery, get the delivery dates
        if delivery_option == "0":
            expected_1 = today_date + timedelta(days=3)
            expected_2 = today_date + timedelta(days=5)
        elif delivery_option == "1":
            expected_1 = today_date + timedelta(days=2)
            expected_2 = today_date + timedelta(days=3)
        else:
            expected_1 = today_date + timedelta(days=3)
            expected_2 = today_date + timedelta(days=5)
        # Get success vault from session
        success_vault = list(request.session.get("vault", []))
        # Set translated vault to an empty string
        translated_vault = []
        # For each item in Vault
        for vault_item in success_vault:
            # Get item from database
            item_per_line = get_object_or_404(Item, pk=vault_item[0])
            # Add price of each item to Subtotal
            price_per_line = (
                item_per_line.price_per_unit
                * int(vault_item[1])
                * int(vault_item[3])
            )
            # Translate each record in vault for template
            translated_vault_item = [
                vault_item[0],
                vault_item[1],
                vault_item[2],
                vault_item[3],
                item_per_line.item_name,
                item_per_line.image_1,
                item_per_line.price_per_unit,
                item_per_line.item_stock,
                price_per_line,
            ]
            # Append translated item to translated vault
            translated_vault.append(translated_vault_item)
        # Clear vault in session
        request.session["vault"] = []
        # Render susses page template
        return render(
            request,
            self.template_name,
            {
                "order_number": order_number,
                "expected_1": expected_1,
                "expected_2": expected_2,
                "translated_vault": translated_vault,
            },
        )
