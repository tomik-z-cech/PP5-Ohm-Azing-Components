# Imports
from django.shortcuts import render, get_object_or_404, redirect  # Responses
from django.views import generic
from items.models import Category
from items.forms import CategoryForm

# Views security
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

# Methods security
from django.contrib.auth.decorators import login_required

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
        all_categories = Category.objects.all()
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
    Class deletes category
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
    
class CreateCategoryView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """
    Class for adding categories
    """
    
    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user.is_superuser

    template_name = "owner/new_category.html"  # Template
    form = CategoryForm  # New bookings form
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
    Class for creating new bookings
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
            },
        )

    def post(self, request, category_pk, *args, **kwargs):
        """
        Function triggers when submit button on booking form is pressed
        """
        edited_category = get_object_or_404(Category, pk=category_pk)
        edit_form = self.form(request.POST, request.FILES)

        if edit_form.is_valid():
            edited_category.category_name = edit_form.cleaned_data["category_name"]
            edited_category.category_image = edit_form.cleaned_data["category_image"]
            edited_category.save()  # Save category into database
        else:
            edit_form = self.form()
        return redirect("owner")  # Redirect back to admin tools