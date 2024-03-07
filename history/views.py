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
    Class for displaying invoices
    """

    template_name = "history/order_history.html"  # Template

    def get(self, request, *args, **kwargs):
        """
        Function generates list of invoices for template
        """
        page_length = int(request.GET.get('page_length', 10))
        page_sort = int(request.GET.get('page_sort', 0))
        current_page = request.GET.get('page', 1)
        if page_length != 0:
            if page_sort == 1:
                paginated_items = Paginator(Order.objects.filter(user=request.user).order_by('-date'), page_length)
            elif page_sort == 0:
                paginated_items = Paginator(Order.objects.filter(user=request.user).order_by('date'), page_length)
            else:
                paginated_items = Paginator(Order.objects.filter(user=request.user).order_by('-date'), page_length)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 1:
                page_obj = Order.objects.filter(user=request.user).order_by('date')
            elif page_sort == 0:
                page_obj = Order.objects.filter(user=request.user).order_by('-date')
            else:
                page_obj = Order.objects.filter(user=request.user).order_by('date')
            paginator_nav = False
        return render(
            request,
            self.template_name,
            {
                "invoices": page_obj,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length":page_length,
            },
        )
class UserViewInvoiceView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        requested_invoice = get_object_or_404(Order, pk=self.kwargs["invoice_pk"])
        return self.request.user == requested_invoice.user
    
    def get(self, request, invoice_pk, *args, **kwargs):
        requested_invoice = get_object_or_404(Order, pk=invoice_pk)
        response = FileResponse(requested_invoice.invoice, content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{requested_invoice.invoice.name}"'
        return response
        
class UserDownloadInvoiceView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    View generates main view for owner (site admin)
    """
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        requested_invoice = get_object_or_404(Order, pk=self.kwargs["invoice_pk"])
        return self.request.user == requested_invoice.user

    def get(self, request, invoice_pk, *args, **kwargs):
        requested_invoice = get_object_or_404(Order, pk=invoice_pk)
        response = FileResponse(requested_invoice.invoice, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{requested_invoice.invoice.name}"'
        return response