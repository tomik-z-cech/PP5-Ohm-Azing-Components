# Imports
import io
import os
import zipfile
from datetime import date
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect  # Responses
from django.views import generic
from django.db.models.functions import Lower
# Views security
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
# Methods security
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, F, ExpressionWrapper, fields
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from items.models import Category, Item, ItemComments
from owner.forms import CategoryForm, ItemForm, PostageSettingsForm, VoucherForm, NewsletterEmailForm
from owner.models import PostageSettings, Voucher, Newsletter, NewsletterEmail
from checkout.models import Order


class OwnerMainView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    View generates main view for owner (site admin)
    """

    template_name = "owner/categories.html"  # Template
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        all_categories = Category.objects.all().order_by(Lower('category_name'))
        return render(
            request,
            self.template_name,
            {
                "all_categories": all_categories,
            },
        )
        
class DeleteCategoryView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for deleting categories
    """
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    @login_required
    def category_delete_request(request, category_pk):
        """This method redirects user to confirm page"""
        requested_category = get_object_or_404(
            Category, pk=category_pk
        )  # Get category
        return render(  # Render template
            request,
            "owner/category_delete_confirm.html",
            {"category_to_delete": requested_category},
        )

    def get(self, request, category_pk, *args, **kwargs):
        """Method GET cancels booking and send confirmation"""
        requested_category = get_object_or_404(
            Category, pk=category_pk
        )  # Get category
        requested_category.delete()  # Delete category from DB
        messages.info(request, f'Category {requested_category.category_name} deleted.')
        return redirect("owner")  # Return to admin tools
    
class AddCategoryView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for adding categories
    """
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    template_name = "owner/new_category.html"  # Template
    form = CategoryForm  # New category form
    success_url = "/owner/"  # URL to redirect after successful creation

    def get(self, request, *args, **kwargs):
        """
        Function generates new category form into template
        """
        return render(
            request,
            self.template_name,
            {
                "new_category_form": CategoryForm(),  # Category form
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Function triggers when add category button pressed
        """
        new_category = self.form(request.POST, request.FILES)
        if new_category.is_valid():
            new_category_name = new_category.cleaned_data['category_name']
            messages.info(request, f'Category {new_category_name} created.')
            new_category.save()  # Save category into database
        else:
            messages.error(request, "Category couldn't be added.")
            new_category = self.form()
        return redirect("owner")  # Redirect back to admin tools
    

class EditCategoryView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing categories
    """

    template_name = "owner/edit_category.html"  # Template
    form = CategoryForm  # Category form
    success_url = "/owner/"  # URL to redirect after successful editing

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, category_pk, *args, **kwargs):
        """
        Function generates category form into template
        """
        category_instance = get_object_or_404(Category, pk=category_pk)
        name_edit_form = category_instance.category_name
        image_edit_form = category_instance.category_image
        category_edit_form = CategoryForm(
            initial={
                "category_name": name_edit_form,
                "category_image": image_edit_form,
            }
        )
        return render(
            request,
            self.template_name,
            {
                "edit_category_form": category_edit_form,  # Edit form
                "category_name": name_edit_form,
                "category_image": image_edit_form,
            },
        )

    def post(self, request, category_pk, *args, **kwargs):
        """
        Function triggers when submit button on category edit form is pressed
        """
        edited_category = get_object_or_404(Category, pk=category_pk)
        edit_form = self.form(request.POST, request.FILES, instance=edited_category)

        if edit_form.is_valid():
            edited_category.category_name = edit_form.cleaned_data["category_name"]
            edited_category.category_image = edit_form.cleaned_data["category_image"]
            edited_category.save()  # Save category into database
            messages.info(request, f'Category {edited_category.category_name} changed.')
        else:
            edit_form = self.form()
            messages.error(request, "Category details couldn't be changed.")
        return redirect("owner")  # Redirect back to admin tools
    

class OwnerItemsView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for creating new bookings
    """

    template_name = "owner/items.html"  # Template

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        page_sort = int(request.GET.get('page_sort', 0))
        page_length = int(request.GET.get('page_length', 10))
        current_page = request.GET.get('page', 1)
        queryset = Item.objects.all().annotate(
            like=Count("item_likes"),
            dislike=Count("item_dislikes"),
            item_likes_num=ExpressionWrapper(
                F('like') - F('dislike'),
                output_field=fields.IntegerField()
                )
            )
        if page_length != 0:
            if page_sort == 7:
                paginated_items = Paginator(queryset.order_by('item_likes_num'), page_length)
            elif page_sort == 6:
                paginated_items = Paginator(queryset.order_by('-item_likes_num'), page_length)
            elif page_sort == 5:
                paginated_items = Paginator(queryset.order_by('-item_stock'), page_length)
            elif page_sort == 4:
                paginated_items = Paginator(queryset.order_by('item_stock'), page_length)
            elif page_sort == 3:
                paginated_items = Paginator(queryset.order_by('-price_per_unit'), page_length)
            elif page_sort == 2:
                paginated_items = Paginator(queryset.order_by('price_per_unit'), page_length)
            elif page_sort == 1:
                paginated_items = Paginator(queryset.order_by('-item_name'), page_length)
            elif page_sort == 0:
                paginated_items = Paginator(queryset.order_by('item_name'), page_length)
            else:
                paginated_items = Paginator(Item.objects.all(), 10)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 7:
                page_obj = queryset.order_by('item_likes_num')
            elif page_sort == 6:
                page_obj = queryset.order_by('-item_likes_num')
            elif page_sort == 5:
                page_obj = queryset.order_by('-item_stock')
            elif page_sort == 4:
                page_obj = queryset.order_by('item_stock')
            elif page_sort == 3:
                page_obj = queryset.order_by('-price_per_unit')
            elif page_sort == 2:
                page_obj = queryset.order_by('price_per_unit')
            elif page_sort == 1:
                page_obj = queryset.order_by('-item_name')
            elif page_sort == 0:
                page_obj = queryset.order_by('item_name')
            else:
                page_obj = Item.objects.all()
            paginator_nav = False
        return render(
            request,
            self.template_name,
            {
                "items": page_obj,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length":page_length,
            },
        )

class AddItemView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for adding items
    """
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    template_name = "owner/new_item.html"  # Template
    form = ItemForm  # New Item form
    success_url = "/owner/"  # URL to redirect after successful creation

    def get(self, request, *args, **kwargs):
        """
        Function generates new item form into template
        """
        return render(
            request,
            self.template_name,
            {
                "new_item_form": ItemForm(),  # Item form
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Function triggers when add category button pressed
        """
        new_item = self.form(request.POST, request.FILES)
        if new_item.is_valid():
            new_item.save()  # Save item into database
            new_item_name = new_item.cleaned_data['item_name']
            messages.info(request, f'Item {new_item_name} added.')
        else:
            new_item = self.form()
            messages.error(request, "Item couldn't be added.")
        return redirect("items")  # Redirect back to admin tools
    
class EditItemView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing items
    """

    template_name = "owner/edit_item.html"  # Template
    form = ItemForm  # Category form
    success_url = "/items/"  # URL to redirect after successful editing

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, item_pk, *args, **kwargs):
        """
        Function generates category form into template
        """
        item_instance = get_object_or_404(Item, pk=item_pk)
        item_edit_form = ItemForm(instance=item_instance)
        return render(
            request,
            self.template_name,
            {
                "edit_item_form": item_edit_form,  # Edit form
                "item_name": item_instance.item_name
            },
        )

    def post(self, request, item_pk, *args, **kwargs):
        """
        Function triggers when submit button on item edit form is pressed
        """
        edited_item = get_object_or_404(Item, pk=item_pk)
        edit_form = self.form(request.POST, request.FILES, instance=edited_item)
        if edit_form.is_valid():
            edit_form.save()  # Save category into database
            messages.info(request, f'Item {edited_item.item_name} changed.')
        else:
            edit_form = self.form()
            messages.error(request, "Item details couldn't be changed.")
        return redirect("items")  # Redirect back to admin tools
    
class DeleteItemView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for deleting items
    """
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    @login_required
    def item_delete_request(request, item_pk):
        """This method redirects user to confirm page"""
        requested_item = get_object_or_404(
            Item, pk=item_pk
        )  # Get Item
        return render(  # Render template
            request,
            "owner/item_delete_confirm.html",
            {"item_to_delete": requested_item},
        )
    
    def get(self, request, item_pk, *args, **kwargs):
        """Method deletes item"""
        requested_item = get_object_or_404(
            Item, pk=item_pk
        )  # Get Item
        requested_item.delete()  # Delete category from DB
        messages.info(request, f'Item {requested_item.item_name} deleted.')
        return redirect("items")  # Return to admin tools
    
class OwnerInvoicesView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for displaying invoices
    """

    template_name = "owner/invoices.html"  # Template

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    def get(self, request, *args, **kwargs):
        """
        Function generates list of invoices for template
        """
        page_length = int(request.GET.get('page_length', 10))
        page_sort = int(request.GET.get('page_sort', 0))
        current_page = request.GET.get('page', 1)
        if page_length != 0:
            if page_sort == 1:
                paginated_items = Paginator(Order.objects.all().order_by('-date'), page_length)
            elif page_sort == 0:
                paginated_items = Paginator(Order.objects.all().order_by('date'), page_length)
            else:
                paginated_items = Paginator(Order.objects.all().order_by('-date'), page_length)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 1:
                page_obj = Order.objects.all().order_by('date')
            elif page_sort == 0:
                page_obj = Order.objects.all().order_by('-date')
            else:
                page_obj = Order.objects.all().order_by('date')
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
        
        
class DownloadInvoiceView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    View generates main view for owner (site admin)
    """

    template_name = "owner/categories.html"  # Template
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, invoice_pk, *args, **kwargs):
        requested_invoice = get_object_or_404(Order, pk=invoice_pk)
        file_name = os.path.basename(requested_invoice.invoice.name)[:-4]
        with requested_invoice.invoice.open(mode='rb') as pdf_file:
            pdf_content = pdf_file.read()
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            zip_file.writestr(f'{file_name}.pdf', pdf_content)
        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={file_name}.zip'
        return response
    
    
class PostageSettingsView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing postage settings
    """

    template_name = "owner/postage.html"  # Template
    success_url = "/owner/"  # URL to redirect after successful editing

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Function generates postage settings form into template
        """
        instance = PostageSettings.objects.filter(pk=1).first()
        settings_form = PostageSettingsForm(instance=instance)
        return render(
            request,
            self.template_name,
            {
                "postage_settings_form": settings_form,
            },
        )
        
    def post(self, request, *args, **kwargs):
        """
        Function saves post settings
        """
        instance = PostageSettings.objects.filter(pk=1).first()
        settings_form = PostageSettingsForm(request.POST, instance=instance)
        if settings_form.is_valid():
            settings_form.save()  # Save category into database
            messages.success(request, 'Postage settings saved.')
        else:
            settings_form = PostageSettingsForm()
            messages.error(request, "Postage settings couldn't be changed.")
        return redirect("owner")  # Redirect back to admin tools
    
    
class CommentsOwnerView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing postage settings
    """

    template_name = "owner/comments-owner.html"  # Template

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    def get(self, request, *args, **kwargs):
        page_length = int(request.GET.get('page_length', 0))
        page_sort = int(request.GET.get('page_sort', 0))
        current_page = request.GET.get('page', 1)
        if page_length != 0:
            if page_sort == 0:
                paginated_items = Paginator(ItemComments.objects.all().order_by('-created_on'), page_length)
            elif page_sort == 1:
                paginated_items = Paginator(ItemComments.objects.filter(approved=1).order_by('-created_on'), page_length)
            elif page_sort == 2:
                paginated_items = Paginator(ItemComments.objects.filter(approved=0).order_by('-created_on'), page_length)
            else:
                paginated_items = Paginator(ItemComments.objects.all().order_by('-created_on'), page_length)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 0:
                page_obj = ItemComments.objects.all().order_by('-created_on')
            elif page_sort == 1:
                page_obj = ItemComments.objects.filter(approved=1).order_by('-created_on')
            elif page_sort == 2:
                page_obj = ItemComments.objects.filter(approved=0).order_by('-created_on')
            else:
                page_obj = ItemComments.objects.all().order_by('-created_on')
            paginator_nav = False
        return render(
            request,
            self.template_name,
            {
                "comments": page_obj,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length": page_length,
            },
        )
        
class DeleteCommentView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for deleting comments
    """
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    @login_required
    def comment_delete_request(request, comment_pk):
        """This method redirects user to confirm page"""
        requested_comment = get_object_or_404(
            ItemComments, pk=comment_pk
        )  # Get Item
        return render(  # Render template
            request,
            "owner/comment_delete_confirm.html",
            {"comment_to_delete": requested_comment},
        )
    
    def get(self, request, comment_pk, *args, **kwargs):
        """Method deletes comment"""
        requested_comment = get_object_or_404(
            ItemComments, pk=comment_pk
        )  # Get Comment
        requested_comment.delete()  # Delete category from DB
        messages.info(request, f'Comment created by {requested_comment.comment_author} deleted.')
        return redirect("comments-owner")  # Return to admin tools
    

class ApproveCommentView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for approving comments
    """
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    def get(self, request, comment_pk, *args, **kwargs):
        """Method approves comment"""
        requested_comment = get_object_or_404(
            ItemComments, pk=comment_pk
        )  # Get Comment
        requested_comment.approved = True
        requested_comment.save()
        messages.info(request, f'Comment created by {requested_comment.comment_author} approved.')
        return redirect("comments-owner")  # Return to admin tools
    
    
class VouchersOwnerView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for managing vouchers
    """

    template_name = "owner/vouchers.html"  # Template

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    def get(self, request, *args, **kwargs):
        page_length = int(request.GET.get('page_length', 0))
        page_sort = int(request.GET.get('page_sort', 0))
        current_page = request.GET.get('page', 1)
        today = date.today()
        if page_length != 0:
            if page_sort == 0:
                paginated_items = Paginator(Voucher.objects.all().order_by('start_date'), page_length)
            elif page_sort == 1:
                paginated_items = Paginator(Voucher.objects.filter(start_date__gt=today).order_by('start_date'), page_length)
            elif page_sort == 2:
                paginated_items = Paginator(Voucher.objects.filter(start_date__lte=today, end_date__gte=today).order_by('start_date'))
            elif page_sort == 3:
                paginated_items = Paginator(Voucher.objects.filter(end_date__lt=today).order_by('start_date'), page_length)
            else:
                paginated_items = Paginator(Voucher.objects.all().order_by('start_date'), page_length)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 0:
                page_obj = Voucher.objects.all().order_by('start_date')
            elif page_sort == 1:
                page_obj = Voucher.objects.filter(start_date__gt=today).order_by('start_date')
            elif page_sort == 2:
                page_obj = Voucher.objects.filter(start_date__lte=today, end_date__gte=today).order_by('start_date')
            elif page_sort == 3:
                page_obj = Voucher.objects.filter(end_date__lt=today).order_by('start_date')
            else:
                page_obj = Voucher.objects.all().order_by('start_date')
            paginator_nav = False
        return render(
            request,
            self.template_name,
            {
                "vouchers": page_obj,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length": page_length,
            },
        )
        
class AddVoucherView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for adding categories
    """
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    template_name = "owner/new_voucher.html"  # Template
    form = VoucherForm  # New voucher form
    success_url = "/vouchers/"  # URL to redirect after successful creation

    def get(self, request, *args, **kwargs):
        """
        Function generates new category form into template
        """
        return render(
            request,
            self.template_name,
            {
                "new_voucher_form": VoucherForm(),  # Category form
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Function triggers when add category button pressed
        """
        new_voucher = self.form(request.POST, request.FILES)
        if new_voucher.is_valid():
            new_voucher_code = new_voucher.cleaned_data['voucher_code']
            messages.info(request, f'Voucher {new_voucher_code} created.')
            new_voucher.save()  # Save category into database
        else:
            messages.error(request, "Voucher couldn't be created.")
            new_voucher = self.form()
        return redirect("vouchers-owner")  # Redirect back to admin tools
    
    
class DeleteVoucherView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for deleting comments
    """
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    @login_required
    def voucher_delete_request(request, voucher_pk):
        """This method redirects user to confirm page"""
        requested_voucher = get_object_or_404(
            Voucher, pk=voucher_pk
        )  # Get Voucher
        return render(  # Render template
            request,
            "owner/voucher_delete_confirm.html",
            {"voucher_to_delete": requested_voucher},
        )
    
    def get(self, request, voucher_pk, *args, **kwargs):
        """Method deletes vocuher"""
        requested_voucher = get_object_or_404(
            Voucher, pk=voucher_pk
        )  # Get Comment
        requested_voucher.delete()  # Delete category from DB
        messages.info(request, f'Voucher {requested_voucher.voucher_code} deleted.')
        return redirect("vouchers-owner")  # Return to admin tools
    
    
class EditVoucherView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing vouchers
    """

    template_name = "owner/edit_voucher.html"  # Template
    form = VoucherForm  # Category form
    success_url = "/vouchers/"  # URL to redirect after successful editing

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, voucher_pk, *args, **kwargs):
        """
        Function generates voucher form into template
        """
        voucher_instance = get_object_or_404(Voucher, pk=voucher_pk)
        voucher_edit_form = VoucherForm(instance=voucher_instance)
        return render(
            request,
            self.template_name,
            {
                "edit_voucher_form": voucher_edit_form,  # Edit form
                "voucher_code": voucher_instance.voucher_code,
            },
        )

    def post(self, request, voucher_pk, *args, **kwargs):
        """
        Function triggers when submit button on category edit form is pressed
        """
        edited_voucher = get_object_or_404(Voucher, pk=voucher_pk)
        edit_form = self.form(request.POST, instance=edited_voucher)

        if edit_form.is_valid():
            edited_voucher.save()  # Save category into database
            messages.info(request, f'Voucher {edited_voucher.voucher_code} changed.')
        else:
            edit_form = self.form()
            messages.error(request, "Voucher details couldn't be changed.")
        return redirect("vouchers-owner")  # Redirect back to admin tools
    
    
class EmailsOwnerView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for sending newsletter emails
    """

    template_name = "owner/newsletter_emails.html"  # Template

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    def get(self, request, *args, **kwargs):
        page_length = int(request.GET.get('page_length', 0))
        page_sort = int(request.GET.get('page_sort', 0))
        current_page = request.GET.get('page', 1)
        if page_length != 0:
            if page_sort == 0:
                paginated_items = Paginator(NewsletterEmail.objects.all().order_by('date_sent'), page_length)
            elif page_sort == 1:
                paginated_items = Paginator(NewsletterEmail.objects.filter(status=0).order_by('date_sent'), page_length)
            elif page_sort == 2:
                paginated_items = Paginator(NewsletterEmail.objects.filter(status=1).order_by('date_sent'), page_length)
            else:
                paginated_items = Paginator(NewsletterEmail.objects.all().order_by('date_sent'), page_length)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 0:
                page_obj = NewsletterEmail.objects.all().order_by('date_sent')
            elif page_sort == 1:
                page_obj = NewsletterEmail.objects.filter(status=0).order_by('date_sent')
            elif page_sort == 2:
                page_obj = NewsletterEmail.objects.filter(status=1).order_by('date_sent')
            else:
                page_obj = NewsletterEmail.objects.all().order_by('date_sent')
            paginator_nav = False
        return render(
            request,
            self.template_name,
            {
                "emails": page_obj,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length": page_length,
            },
        )
        
class NewEmailView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for creating new newsletter email
    """
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    template_name = "owner/new_email.html"  # Template
    form = NewsletterEmail  # New voucher form
    success_url = "/emails/"  # URL to redirect after successful creation

    def get(self, request, *args, **kwargs):
        """
        Function generates new email form into template
        """
        return render(
            request,
            self.template_name,
            {
                "new_email_form": NewsletterEmailForm(),  # Category form
            },
        )
        
    def post(self, request, *args, **kwargs):
        new_email = NewsletterEmailForm(request.POST)
        if 'save' in request.POST:
            if new_email.is_valid():
                new_email.save()
                messages.info(request, f'Email saved as draft.')
            else:
                new_email = NewsletterEmailForm()
        elif 'send' in request.POST:
            if new_email.is_valid():
                new_email.instance.date_sent = date.today()
                new_email.instance.status = 1
                new_email.save()
                # Add email of user creating booking
                email_addresses = Newsletter.objects.all()
                subject = new_email.instance.subject  # Subject
                from_address = "ohmazingcomponents@gmail.com"  # From
                for email_address in email_addresses:
                    recipient = []
                    recipient.append(email_address.newsletter_email)
                    html_message = render_to_string(
                        "emails/newsletter_template.html",
                        {
                            "user": email_address.newsletter_email,
                            "body": new_email.instance.body
                        },
                    )
                    message = strip_tags(html_message)
                    send_mail(
                        subject,
                        message,
                        from_address,
                        recipient,
                        html_message=html_message
                    )
                    messages.info(request, f'Email sent to {len(email_addresses)} recipients.')
        else:
            new_email = NewsletterEmailForm()
        return redirect("emails-owner")  # Redirect back to admin tools
    
class DeleteEmailView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for deleting emails
    """
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser
    
    @login_required
    def email_delete_request(request, email_pk):
        """This method redirects user to confirm page"""
        requested_email = get_object_or_404(
            NewsletterEmail, pk=email_pk
        )  # Get Voucher
        return render(  # Render template
            request,
            "owner/email_delete_confirm.html",
            {"email_to_delete": requested_email},
        )
    
    def get(self, request, email_pk, *args, **kwargs):
        """Method deletes email draft"""
        requested_email = get_object_or_404(
            NewsletterEmail, pk=email_pk
        )  # Get Comment
        requested_email.delete()  # Delete category from DB
        messages.info(request, 'Email draft deleted.')
        return redirect("emails-owner")  # Return to admin tools
    
    
class EditEmailView(
        UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing emails
    """

    template_name = "owner/edit_email.html"  # Template
    form = NewsletterEmailForm  # Category form
    success_url = "/emails/"  # URL to redirect after successful editing

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, email_pk, *args, **kwargs):
        """
        Function generates email form into template
        """
        email_instance = get_object_or_404(NewsletterEmail, pk=email_pk)
        email_edit_form = NewsletterEmailForm(instance=email_instance)
        return render(
            request,
            self.template_name,
            {
                "edit_email_form": email_edit_form,  # Edit form
                "email_subject": email_instance.subject,
            },
        )

    def post(self, request, email_pk, *args, **kwargs):
        """
        Function triggers when submit button on category edit form is pressed
        """
        edited_email_instance = NewsletterEmail(pk=email_pk)
        edited_email = NewsletterEmailForm(request.POST, instance=edited_email_instance)
        if 'save' in request.POST:
            if edited_email.is_valid():
                edited_email.instance.date_sent = date.today()
                edited_email.save()
                messages.info(request, f'Edited email saved as draft.')
            else:
                edited_email = NewsletterEmailForm()
        elif 'send' in request.POST:
            if edited_email.is_valid():
                edited_email.instance.date_sent = date.today()
                edited_email.instance.status = 1
                edited_email.save()
                # Add email of user creating booking
                email_addresses = Newsletter.objects.all()
                subject = edited_email.instance.subject  # Subject
                from_address = "ohmazingcomponents@gmail.com"  # From
                for email_address in email_addresses:
                    recipient = []
                    recipient.append(email_address.newsletter_email)
                    html_message = render_to_string(
                        "emails/newsletter_template.html",
                        {
                            "user": email_address.newsletter_email,
                            "body": edited_email.instance.body
                        },
                    )
                    message = strip_tags(html_message)
                    send_mail(
                        subject,
                        message,
                        from_address,
                        recipient,
                        html_message=html_message
                    )
                    messages.info(request, f'Email sent to {len(email_addresses)} recipients.')
        else:
            edited_email = NewsletterEmailForm()
        return redirect("emails-owner")  # Redirect back to admin tools