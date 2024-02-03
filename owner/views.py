# Imports
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
from items.models import Category, Item
from items.forms import CategoryForm, ItemForm



# Create your views here.
class OwnerMainView(generic.ListView, LoginRequiredMixin, UserPassesTestMixin):
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
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
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
        return redirect("owner")  # Return to admin tools
    
class AddCategoryView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
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
            new_category.save()  # Save category into database
        else:
            new_category = self.form()
        return redirect("owner")  # Redirect back to admin tools
    

class EditCategoryView(
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
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
        else:
            edit_form = self.form()
        return redirect("owner")  # Redirect back to admin tools
    

class OwnerItemsView(
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """
    Class for creating new bookings
    """

    template_name = "owner/items.html"  # Template

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        all_items = Item.objects.all()
        return render(
            request,
            self.template_name,
            {
                "items": all_items,
            },
        )
        
class AddItemView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
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
        new_category = self.form(request.POST, request.FILES)
        if new_category.is_valid():
            new_category.save()  # Save category into database
        else:
            new_category = self.form()
        return redirect("items")  # Redirect back to admin tools
    
class EditItemView(
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
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
            edited_item.save()  # Save category into database
        else:
            edit_form = self.form()
        return redirect("items")  # Redirect back to admin tools
    
class DeleteItemView(
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
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
        """Method GET cancels booking and send confirmation"""
        requested_item = get_object_or_404(
            Item, pk=item_pk
        )  # Get Item
        requested_item.delete()  # Delete category from DB
        return redirect("items")  # Return to admin tools