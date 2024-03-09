# PEP8
# Imports
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Views security
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.core.paginator import Paginator
from django.http import FileResponse
from checkout.models import Order


# Create your views here.
class UserInvoicesView(LoginRequiredMixin, generic.ListView):
    """
    Class for displaying invoices for user
    """

    template_name = "history/order_history.html"  # Template

    def get(self, request, *args, **kwargs):
        """
        Function generates list of user's invoices for template
        """
        # Pagination initial settings
        page_length = int(request.GET.get("page_length", 10))
        page_sort = int(request.GET.get("page_sort", 0))
        current_page = request.GET.get("page", 1)
        # Get data of invoices based on page_sort and page_length
        if page_length != 0:
            if page_sort == 1:
                paginated_items = Paginator(
                    Order.objects.filter(user=request.user).order_by("-date"),
                    page_length,
                )
            elif page_sort == 0:
                paginated_items = Paginator(
                    Order.objects.filter(user=request.user).order_by("date"),
                    page_length,
                )
            else:
                paginated_items = Paginator(
                    Order.objects.filter(user=request.user).order_by("-date"),
                    page_length,
                )
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 1:
                page_obj = Order.objects.filter(user=request.user).order_by(
                    "date"
                )
            elif page_sort == 0:
                page_obj = Order.objects.filter(user=request.user).order_by(
                    "-date"
                )
            else:
                page_obj = Order.objects.filter(user=request.user).order_by(
                    "date"
                )
            paginator_nav = False
        # Render template with objects
        return render(
            request,
            self.template_name,
            {
                "invoices": page_obj,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length": page_length,
            },
        )


class UserViewInvoiceView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for viewing user's invoices in browser
    """

    def test_func(self):
        """Test function to ensure user is the customer of invoice"""
        requested_invoice = get_object_or_404(
            Order, pk=self.kwargs["invoice_pk"]
        )
        return self.request.user == requested_invoice.user

    def get(self, request, invoice_pk, *args, **kwargs):
        """
        Method finds and displays invoice to the user
        """
        # Get requestee invoice from database
        requested_invoice = get_object_or_404(Order, pk=invoice_pk)
        # Create response as file for viewing in browser
        response = FileResponse(
            requested_invoice.invoice, content_type="application/pdf"
        )
        response["Content-Disposition"] = (
            f'filename="{requested_invoice.invoice.name}"'
        )
        # Return response to browser
        return response


class UserDownloadInvoiceView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class is used to download users selected invoice
    """

    def test_func(self):
        """
        Test function to ensure the reuqested invoice is the users order
        """
        requested_invoice = get_object_or_404(
            Order, pk=self.kwargs["invoice_pk"]
        )
        return self.request.user == requested_invoice.user

    def get(self, request, invoice_pk, *args, **kwargs):
        """
        Method is user to find and generate download response of users invoice
        """
        # Pull invoice from database
        requested_invoice = get_object_or_404(Order, pk=invoice_pk)
        # Create response with file download
        response = FileResponse(
            requested_invoice.invoice, content_type="application/pdf"
        )
        response["Content-Disposition"] = (
            f'attachment; filename="{requested_invoice.invoice.name}"'
        )
        # Return response to browser
        return response
