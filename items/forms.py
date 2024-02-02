# Imports
from django import forms
from owner.widgets import CustomClearableFileInput
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
        
    category_image = forms.ImageField(label='Category Image', required=False, widget=CustomClearableFileInput)