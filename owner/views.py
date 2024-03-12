# PEP8
# Imports
from datetime import date
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
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
from django.http import FileResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from items.models import Category, Item, ItemComments
from owner.forms import (
    CategoryForm,
    ItemForm,
    PostageSettingsForm,
    VoucherForm,
    NewsletterEmailForm,
)
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
        """
        Method creates initial admin view (categories)
        """
        # Get all categories from databse
        all_categories = Category.objects.all().order_by(
            Lower("category_name")
        )
        # Render template
        return render(
            request,
            self.template_name,
            {
                "all_categories": all_categories,
            },
        )


class DeleteCategoryView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for deleting categories
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    @login_required
    def category_delete_request(request, category_pk):
        """This method redirects user to confirm page of deleting category"""
        # Get requested category
        requested_category = get_object_or_404(Category, pk=category_pk)
        # Render template
        return render(
            request,
            "owner/category_delete_confirm.html",
            {"category_to_delete": requested_category},
        )

    def get(self, request, category_pk, *args, **kwargs):
        """
        Method GET deletes category
        """
        # Get requested category
        requested_category = get_object_or_404(Category, pk=category_pk)
        # Delete requested category
        requested_category.delete()
        messages.info(
            request, f"Category {requested_category.category_name} deleted."
        )
        # Redirect back to admin tools
        return redirect("owner")


class AddCategoryView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
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
        # Render template
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
        # Get details of new category from form and get files
        new_category = self.form(request.POST, request.FILES)
        # If the form is valid
        if new_category.is_valid():
            new_category_name = new_category.cleaned_data["category_name"]
            messages.info(request, f"Category {new_category_name} created.")
            # Save new category into database
            new_category.save()  # Save category into database
        # If not valid send same data back
        else:
            messages.error(request, "Category couldn't be added.")
            new_category = self.form()
        # Redirect back to admin tools
        return redirect("owner")


class EditCategoryView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for editing categories
    """

    template_name = "owner/edit_category.html"
    form = CategoryForm
    success_url = "/owner/"

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, category_pk, *args, **kwargs):
        """
        Function generates category details into template
        """
        # Get the category to edit
        category_instance = get_object_or_404(Category, pk=category_pk)
        # Get the initial name and image
        name_edit_form = category_instance.category_name
        image_edit_form = category_instance.category_image
        # Prefill the edit form
        category_edit_form = CategoryForm(
            initial={
                "category_name": name_edit_form,
                "category_image": image_edit_form,
            }
        )
        # Render edititng template
        return render(
            request,
            self.template_name,
            {
                "edit_category_form": category_edit_form,
                "category_name": name_edit_form,
                "category_image": image_edit_form,
            },
        )

    def post(self, request, category_pk, *args, **kwargs):
        """
        Function triggers when submit button on category edit form is pressed
        """
        # Get the edited category from database
        edited_category = get_object_or_404(Category, pk=category_pk)
        # Get POSTED edit form and files
        edit_form = self.form(
            request.POST, request.FILES, instance=edited_category
        )
        # If edit form is valid
        if edit_form.is_valid():
            # Change name and image
            edited_category.category_name = edit_form.cleaned_data[
                "category_name"
            ]
            edited_category.category_image = edit_form.cleaned_data[
                "category_image"
            ]
            # Save edited category into database
            edited_category.save()
            messages.info(
                request, f"Category {edited_category.category_name} changed."
            )
        # Edited category form is not valid
        else:
            # Return form back to template
            edit_form = self.form()
            messages.error(request, "Category details couldn't be changed.")
        # Redirect back to admin tools
        return redirect("owner")


class OwnerItemsView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for viewing shop items
    """

    template_name = "owner/items.html"  # Template

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Method is to generate data for lis of items view
        """
        # Inital values for pagination
        page_sort = int(request.GET.get("page_sort", 0))
        page_length = int(request.GET.get("page_length", 10))
        current_page = request.GET.get("page", 1)
        # Initial queryset
        queryset = Item.objects.all().annotate(
            like=Count("item_likes"),
            dislike=Count("item_dislikes"),
            item_likes_num=ExpressionWrapper(
                F("like") - F("dislike"), output_field=fields.IntegerField()
            ),
        )
        # Soting an pagination options and querysets
        if page_length != 0:
            if page_sort == 7:
                paginated_items = Paginator(
                    queryset.order_by("item_likes_num"), page_length
                )
            elif page_sort == 6:
                paginated_items = Paginator(
                    queryset.order_by("-item_likes_num"), page_length
                )
            elif page_sort == 5:
                paginated_items = Paginator(
                    queryset.order_by("-item_stock"), page_length
                )
            elif page_sort == 4:
                paginated_items = Paginator(
                    queryset.order_by("item_stock"), page_length
                )
            elif page_sort == 3:
                paginated_items = Paginator(
                    queryset.order_by("-price_per_unit"), page_length
                )
            elif page_sort == 2:
                paginated_items = Paginator(
                    queryset.order_by("price_per_unit"), page_length
                )
            elif page_sort == 1:
                paginated_items = Paginator(
                    queryset.order_by("-item_name"), page_length
                )
            elif page_sort == 0:
                paginated_items = Paginator(
                    queryset.order_by("item_name"), page_length
                )
            else:
                paginated_items = Paginator(Item.objects.all(), 10)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 7:
                page_obj = queryset.order_by("item_likes_num")
            elif page_sort == 6:
                page_obj = queryset.order_by("-item_likes_num")
            elif page_sort == 5:
                page_obj = queryset.order_by("-item_stock")
            elif page_sort == 4:
                page_obj = queryset.order_by("item_stock")
            elif page_sort == 3:
                page_obj = queryset.order_by("-price_per_unit")
            elif page_sort == 2:
                page_obj = queryset.order_by("price_per_unit")
            elif page_sort == 1:
                page_obj = queryset.order_by("-item_name")
            elif page_sort == 0:
                page_obj = queryset.order_by("item_name")
            else:
                page_obj = Item.objects.all()
            paginator_nav = False
        # Render template
        return render(
            request,
            self.template_name,
            {
                "items": page_obj,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length": page_length,
            },
        )


class AddItemView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for adding items
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    template_name = "owner/new_item.html"
    form = ItemForm

    def get(self, request, *args, **kwargs):
        """
        Function generates new item form into template
        """
        # Render template
        return render(
            request,
            self.template_name,
            {
                "new_item_form": ItemForm(),  # Item form
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Function triggers when add item button pressed
        """
        # Get new item details and files from POST request
        new_item = self.form(request.POST, request.FILES)
        # If the form is valid
        if new_item.is_valid():
            # Save item into database
            new_item.save()
            new_item_name = new_item.cleaned_data["item_name"]
            messages.info(request, f"Item {new_item_name} added.")
        # Form not valid
        else:
            # Returned prefilled form into template
            new_item = self.form()
            messages.error(request, "Item couldn't be added.")
        return redirect("items")


class EditItemView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing items
    """

    template_name = "owner/edit_item.html"
    form = ItemForm

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, item_pk, *args, **kwargs):
        """
        Function generates itme form into template
        """
        # Get edited item
        item_instance = get_object_or_404(Item, pk=item_pk)
        # Prefill edit form
        item_edit_form = ItemForm(instance=item_instance)
        # Render template
        return render(
            request,
            self.template_name,
            {
                "edit_item_form": item_edit_form,  # Edit form
                "item_name": item_instance.item_name,
            },
        )

    def post(self, request, item_pk, *args, **kwargs):
        """
        Function triggers when submit button on item edit form is pressed
        """
        # Get edited item from database
        edited_item = get_object_or_404(Item, pk=item_pk)
        # Get details and files from request.POST
        edit_form = self.form(
            request.POST, request.FILES, instance=edited_item
        )
        # If form valid
        if edit_form.is_valid():
            # Save detials to database
            edit_form.save()
            messages.info(request, f"Item {edited_item.item_name} changed.")
        # Form not valid
        else:
            # Send form back to template
            edit_form = self.form()
            messages.error(request, "Item details couldn't be changed.")
        # Redirect back to admin tools
        return redirect("items")


class DeleteItemView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for deleting items
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    @login_required
    def item_delete_request(request, item_pk):
        """This method redirects user to confirm page of deleting item"""
        # Get requested item
        requested_item = get_object_or_404(Item, pk=item_pk)
        # Render template
        return render(
            request,
            "owner/item_delete_confirm.html",
            {"item_to_delete": requested_item},
        )

    def get(self, request, item_pk, *args, **kwargs):
        """Method deletes item"""
        # Get item from database
        requested_item = get_object_or_404(Item, pk=item_pk)
        # Delete requested item from database
        requested_item.delete()
        messages.info(request, f"Item {requested_item.item_name} deleted.")
        # Return back to admin tools
        return redirect("items")


class OwnerInvoicesView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for displaying all invoices
    """

    template_name = "owner/invoices.html"

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Function generates list of invoices for template
        """
        # Sorting and paginating starting setup
        page_length = int(request.GET.get("page_length", 10))
        page_sort = int(request.GET.get("page_sort", 0))
        current_page = request.GET.get("page", 1)
        # Sorting and paginating querysets
        if page_length != 0:
            if page_sort == 1:
                paginated_items = Paginator(
                    Order.objects.all().order_by("-date"), page_length
                )
            elif page_sort == 0:
                paginated_items = Paginator(
                    Order.objects.all().order_by("date"), page_length
                )
            else:
                paginated_items = Paginator(
                    Order.objects.all().order_by("-date"), page_length
                )
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 1:
                page_obj = Order.objects.all().order_by("date")
            elif page_sort == 0:
                page_obj = Order.objects.all().order_by("-date")
            else:
                page_obj = Order.objects.all().order_by("date")
            paginator_nav = False
        # Render template
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


class ViewInvoiceView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for viewing invoices in the browser
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, invoice_pk, *args, **kwargs):
        """
        Method render pdf file into File response
        """
        # Get the requested invoice
        requested_invoice = get_object_or_404(Order, pk=invoice_pk)
        # pdf file into browser response
        response = FileResponse(
            requested_invoice.invoice, content_type="application/pdf"
        )
        response["Content-Disposition"] = (
            f'filename="{requested_invoice.invoice.name}"'
        )
        # Return response
        return response


class DownloadInvoiceView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class generates downloadable pdf file
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, invoice_pk, *args, **kwargs):
        """
        Method renders file into attachement response
        """
        # Get requested invoice
        requested_invoice = get_object_or_404(Order, pk=invoice_pk)
        # Render file into attachement (downloadable)
        response = FileResponse(
            requested_invoice.invoice, content_type="application/pdf"
        )
        response["Content-Disposition"] = (
            f'attachment; filename="{requested_invoice.invoice.name}"'
        )
        # Return response
        return response


class PostageSettingsView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for editing postage settings
    """

    template_name = "owner/postage.html"

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Function generates postage settings form into template
        """
        # Select the only one instance of postage settings
        instance = PostageSettings.objects.filter(pk=1).first()
        # Pre-fill the form with saved info
        settings_form = PostageSettingsForm(instance=instance)
        # Render template
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
        # Get the post settings only instance
        instance = PostageSettings.objects.filter(pk=1).first()
        # Get post settings form from request.POST
        settings_form = PostageSettingsForm(request.POST, instance=instance)
        # If form is valid
        if settings_form.is_valid():
            # Save settings form
            settings_form.save()  # Save category into database
            messages.success(request, "Postage settings saved.")
        # Form not valid
        else:
            # Clear form
            settings_form = PostageSettingsForm()
            messages.error(request, "Postage settings couldn't be changed.")
        # Redirect back to admin tools
        return redirect("owner")


class CommentsOwnerView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for managing users comments
    """

    template_name = "owner/comments_owner.html"

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Method reads all comments submitted and renders them to template
        """
        # Initial pagination settings
        page_length = int(request.GET.get("page_length", 0))
        page_sort = int(request.GET.get("page_sort", 0))
        current_page = request.GET.get("page", 1)
        # Sorting and paginations querysets
        if page_length != 0:
            if page_sort == 0:
                paginated_items = Paginator(
                    ItemComments.objects.all().order_by("-created_on"),
                    page_length,
                )
            elif page_sort == 1:
                paginated_items = Paginator(
                    ItemComments.objects.filter(approved=1).order_by(
                        "-created_on"
                    ),
                    page_length,
                )
            elif page_sort == 2:
                paginated_items = Paginator(
                    ItemComments.objects.filter(approved=0).order_by(
                        "-created_on"
                    ),
                    page_length,
                )
            else:
                paginated_items = Paginator(
                    ItemComments.objects.all().order_by("-created_on"),
                    page_length,
                )
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 0:
                page_obj = ItemComments.objects.all().order_by("-created_on")
            elif page_sort == 1:
                page_obj = ItemComments.objects.filter(approved=1).order_by(
                    "-created_on"
                )
            elif page_sort == 2:
                page_obj = ItemComments.objects.filter(approved=0).order_by(
                    "-created_on"
                )
            else:
                page_obj = ItemComments.objects.all().order_by("-created_on")
            paginator_nav = False
        # Render template
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
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for deleting comments
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    @login_required
    def comment_delete_request(request, comment_pk):
        """
        This method redirects user to confirm page of deleting comment
        """
        # Get requested comment
        requested_comment = get_object_or_404(ItemComments, pk=comment_pk)
        # Render confirmation template
        return render(
            request,
            "owner/comment_delete_confirm.html",
            {"comment_to_delete": requested_comment},
        )

    def get(self, request, comment_pk, *args, **kwargs):
        """
        Method deletes comment
        """
        # Get requested comment
        requested_comment = get_object_or_404(ItemComments, pk=comment_pk)
        # Delete comment
        requested_comment.delete()  # Delete category from DB
        messages.info(
            request,
            f"Comment created by {requested_comment.comment_author} deleted.",
        )
        # Return back to admin tools
        return redirect("comments-owner")


class ApproveCommentView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for approving comments
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, comment_pk, *args, **kwargs):
        """
        Method approves comments
        """
        # Get requested comment
        requested_comment = get_object_or_404(ItemComments, pk=comment_pk)
        # Set requested comment as approved
        requested_comment.approved = True
        # Save the settings
        requested_comment.save()
        messages.info(
            request,
            f"Comment created by {requested_comment.comment_author} approved.",
        )
        # Return to admin tools
        return redirect("comments-owner")


class VouchersOwnerView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for managing vouchers
    """

    template_name = "owner/vouchers.html"

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Method gets list of vouchers and renders template
        """
        # Sorting and pagination settings
        page_length = int(request.GET.get("page_length", 0))
        page_sort = int(request.GET.get("page_sort", 0))
        current_page = request.GET.get("page", 1)
        # Todays date
        today = date.today()
        # Sorting and paginations options and querysets
        if page_length != 0:
            if page_sort == 0:
                paginated_items = Paginator(
                    Voucher.objects.all().order_by("start_date"), page_length
                )
            elif page_sort == 1:
                paginated_items = Paginator(
                    Voucher.objects.filter(start_date__gt=today).order_by(
                        "start_date"
                    ),
                    page_length,
                )
            elif page_sort == 2:
                paginated_items = Paginator(
                    Voucher.objects.filter(
                        start_date__lte=today, end_date__gte=today
                    ).order_by("start_date")
                )
            elif page_sort == 3:
                paginated_items = Paginator(
                    Voucher.objects.filter(end_date__lt=today).order_by(
                        "start_date"
                    ),
                    page_length,
                )
            else:
                paginated_items = Paginator(
                    Voucher.objects.all().order_by("start_date"), page_length
                )
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 0:
                page_obj = Voucher.objects.all().order_by("start_date")
            elif page_sort == 1:
                page_obj = Voucher.objects.filter(
                    start_date__gt=today
                ).order_by("start_date")
            elif page_sort == 2:
                page_obj = Voucher.objects.filter(
                    start_date__lte=today, end_date__gte=today
                ).order_by("start_date")
            elif page_sort == 3:
                page_obj = Voucher.objects.filter(end_date__lt=today).order_by(
                    "start_date"
                )
            else:
                page_obj = Voucher.objects.all().order_by("start_date")
            paginator_nav = False
        # Render template
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


class AddVoucherView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for adding vouchers to database
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    template_name = "owner/new_voucher.html"
    form = VoucherForm

    def get(self, request, *args, **kwargs):
        """
        Function generates new voucher form into template
        """
        # Render template
        return render(
            request,
            self.template_name,
            {
                "new_voucher_form": VoucherForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Function triggers when add voucher button pressed
        """
        # Get new voucher from request.POST
        new_voucher = self.form(request.POST, request.FILES)
        # If vocuher form valid
        if new_voucher.is_valid():
            # Get voucher name
            new_voucher_code = new_voucher.cleaned_data["voucher_code"]
            messages.info(request, f"Voucher {new_voucher_code} created.")
            # Save new voucher into database
            new_voucher.save()
        # If form not valid
        else:
            messages.error(request, "Voucher couldn't be created.")
            # Reset form
            new_voucher = self.form()
        # Redicrect back to admin tools
        return redirect("vouchers-owner")


class DeleteVoucherView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for deleting vouchers
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    @login_required
    def voucher_delete_request(request, voucher_pk):
        """
        This method redirects user to confirm page of deleting voucher
        """
        # Get requested voucher
        requested_voucher = get_object_or_404(Voucher, pk=voucher_pk)
        # Render template
        return render(
            request,
            "owner/voucher_delete_confirm.html",
            {"voucher_to_delete": requested_voucher},
        )

    def get(self, request, voucher_pk, *args, **kwargs):
        """
        Method deletes voucher
        """
        # Get voucher
        requested_voucher = get_object_or_404(Voucher, pk=voucher_pk)
        # Delete voucher from database
        requested_voucher.delete()
        messages.info(
            request, f"Voucher {requested_voucher.voucher_code} deleted."
        )
        # Return to admin tools
        return redirect("vouchers-owner")


class EditVoucherView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for editing vouchers
    """

    template_name = "owner/edit_voucher.html"
    form = VoucherForm

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, voucher_pk, *args, **kwargs):
        """
        Function generates voucher form into template
        """
        # Get voucher for editing
        voucher_instance = get_object_or_404(Voucher, pk=voucher_pk)
        # Prefill info into voucher form
        voucher_edit_form = VoucherForm(instance=voucher_instance)
        # Render template
        return render(
            request,
            self.template_name,
            {
                "edit_voucher_form": voucher_edit_form,
                "voucher_code": voucher_instance.voucher_code,
            },
        )

    def post(self, request, voucher_pk, *args, **kwargs):
        """
        Function triggers when submit button on voucher edit form is pressed
        """
        # Get edited voucher
        edited_voucher = get_object_or_404(Voucher, pk=voucher_pk)
        # Get voucher data from request.POST
        edit_form = self.form(request.POST, instance=edited_voucher)
        # If form is valid
        if edit_form.is_valid():
            # Save voucher details into database
            edited_voucher.save()
            messages.info(
                request, f"Voucher {edited_voucher.voucher_code} changed."
            )
        # Form not valid
        else:
            # Reset vocuher form
            edit_form = self.form()
            messages.error(request, "Voucher details couldn't be changed.")
        # Redirect back to admin tools
        return redirect("vouchers-owner")


class EmailsOwnerView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for sending newsletter emails
    """

    template_name = "owner/newsletter_emails.html"

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Method gets list of newsletter emails to render to template
        """
        # Sorting a pagination initial variables
        page_length = int(request.GET.get("page_length", 0))
        page_sort = int(request.GET.get("page_sort", 0))
        current_page = request.GET.get("page", 1)
        # Page sort and pagination querysets
        if page_length != 0:
            if page_sort == 0:
                paginated_items = Paginator(
                    NewsletterEmail.objects.all().order_by("date_sent"),
                    page_length,
                )
            elif page_sort == 1:
                paginated_items = Paginator(
                    NewsletterEmail.objects.filter(status=0).order_by(
                        "date_sent"
                    ),
                    page_length,
                )
            elif page_sort == 2:
                paginated_items = Paginator(
                    NewsletterEmail.objects.filter(status=1).order_by(
                        "date_sent"
                    ),
                    page_length,
                )
            else:
                paginated_items = Paginator(
                    NewsletterEmail.objects.all().order_by("date_sent"),
                    page_length,
                )
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 0:
                page_obj = NewsletterEmail.objects.all().order_by("date_sent")
            elif page_sort == 1:
                page_obj = NewsletterEmail.objects.filter(status=0).order_by(
                    "date_sent"
                )
            elif page_sort == 2:
                page_obj = NewsletterEmail.objects.filter(status=1).order_by(
                    "date_sent"
                )
            else:
                page_obj = NewsletterEmail.objects.all().order_by("date_sent")
            paginator_nav = False
        # Render template
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

    template_name = "owner/new_email.html"
    form = NewsletterEmail

    def get(self, request, *args, **kwargs):
        """
        Function generates new email form into template
        """
        # Render template
        return render(
            request,
            self.template_name,
            {
                "new_email_form": NewsletterEmailForm(),  # Category form
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Method saves email as draft or sends the email
        """
        # Get content of new email from request.POST
        new_email = NewsletterEmailForm(request.POST)
        # If save requested by user ...
        if "save" in request.POST:
            # ... and form is valid
            if new_email.is_valid():
                # Save the email as draft
                new_email.save()
                messages.info(request, f"Email saved as draft.")
            # Form not valid, reset form
            else:
                new_email = NewsletterEmailForm()
        # If send requested by user ...
        elif "send" in request.POST:
            # ... and form is valid
            if new_email.is_valid():
                # Set sent day as today
                new_email.instance.date_sent = date.today()
                # Set status as sent
                new_email.instance.status = 1
                # Save email into database
                new_email.save()
                # Add emails of all users receiving newsletters
                email_addresses = Newsletter.objects.all()
                # Set subject of email
                subject = new_email.instance.subject
                # Set from address
                from_address = "ohmazingcomponents@gmail.com"
                # Loop through all users receiving emails and send email
                for email_address in email_addresses:
                    # Set current recepient
                    recipient = email_address.newsletter_email
                    # Render HTML template to string with context
                    html_message = render_to_string(
                        "emails/newsletter_template.html",
                        {
                            "user": email_address.newsletter_email,
                            "body": new_email.instance.body,
                        },
                    )
                    # Fallback message without HTML tags
                    message = strip_tags(html_message)
                    # Send email
                    send_mail(
                        subject,
                        message,
                        from_address,
                        recipient,
                        html_message=html_message,
                    )
                    messages.info(
                        request,
                        f"Email sent to {len(email_addresses)} recipients.",
                    )
            # Form not valid, reset form
            else:
                new_email = NewsletterEmailForm()
        # Form not valid, reset form
        else:
            new_email = NewsletterEmailForm()
        # Redirect back to admin tools
        return redirect("emails-owner")


class DeleteEmailView(
    UserPassesTestMixin, LoginRequiredMixin, generic.ListView
):
    """
    Class for deleting emails
    """

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    @login_required
    def email_delete_request(request, email_pk):
        """
        This method redirects user to confirm page of email drafts deletition
        """
        # Get requested email
        requested_email = get_object_or_404(NewsletterEmail, pk=email_pk)
        # Render template
        return render(
            request,
            "owner/email_delete_confirm.html",
            {"email_to_delete": requested_email},
        )

    def get(self, request, email_pk, *args, **kwargs):
        """
        Method deletes email draft
        """
        # Get email draft
        requested_email = get_object_or_404(NewsletterEmail, pk=email_pk)
        # Delete email draft from database
        requested_email.delete()
        messages.info(request, "Email draft deleted.")
        # Return back to admin tools
        return redirect("emails-owner")


class EditEmailView(UserPassesTestMixin, LoginRequiredMixin, generic.ListView):
    """
    Class for editing email drafts
    """

    template_name = "owner/edit_email.html"
    form = NewsletterEmailForm

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, email_pk, *args, **kwargs):
        """
        Function generates email draft into template
        """
        # Get email draft
        email_instance = get_object_or_404(NewsletterEmail, pk=email_pk)
        # Prefill draft instance into form
        email_edit_form = NewsletterEmailForm(instance=email_instance)
        # Render template
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
        Function triggers when save or send
        button on email edit form is pressed
        """
        # Get the instance of edited email
        edited_email_instance = NewsletterEmail(pk=email_pk)
        # Get form content from request.POST
        edited_email = NewsletterEmailForm(
            request.POST, instance=edited_email_instance
        )
        # If save in user request ...
        if "save" in request.POST:
            # ... and form is valid
            if edited_email.is_valid():
                # Update editing date as today
                edited_email.instance.date_sent = date.today()
                # Save draft into database
                edited_email.save()
                messages.info(request, f"Edited email saved as draft.")
            # Form not valid
            else:
                # Reset form
                edited_email = NewsletterEmailForm()
        # If send in users request ...
        elif "send" in request.POST:
            # ... and form is valid
            if edited_email.is_valid():
                # Update sent date
                edited_email.instance.date_sent = date.today()
                # Update email status
                edited_email.instance.status = 1
                # Save email into database
                edited_email.save()
                # Gather emails of all users receiving emails
                email_addresses = Newsletter.objects.all()
                # Set subject
                subject = edited_email.instance.subject
                # Set from email address
                from_address = "ohmazingcomponents@gmail.com"
                # Loop for sending emails
                for email_address in email_addresses:
                    recipient = email_address.newsletter_email
                    # Render HTML template into string
                    html_message = render_to_string(
                        "emails/newsletter_template.html",
                        {
                            "user": email_address.newsletter_email,
                            "body": edited_email.instance.body,
                        },
                    )
                    # Fallback message
                    message = strip_tags(html_message)
                    # Send email
                    send_mail(
                        subject,
                        message,
                        from_address,
                        recipient,
                        html_message=html_message,
                    )
                    messages.info(
                        request,
                        f"Email sent to {len(email_addresses)} recipients.",
                    )
            # Form not valid
            else:
                # Reset form
                edited_email = NewsletterEmailForm()
        # Form not valid
        else:
            # Reset form
            edited_email = NewsletterEmailForm()
        # Redirect back to admin tools
        return redirect("emails-owner")
