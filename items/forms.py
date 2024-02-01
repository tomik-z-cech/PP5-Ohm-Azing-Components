# Imports
from django import forms
from items.models import Category

class CategoryForm(forms.ModelForm):
    """
    Category form
    """
    class Meta:
        model = Category
        fields = (
            "category_name",
            "category_image",
        )