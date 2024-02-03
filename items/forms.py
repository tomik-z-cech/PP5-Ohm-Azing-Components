# Imports
from django import forms
from owner.widgets import CustomImageInputCategory
from items.models import Category, Item

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
        
    category_image = forms.ImageField(label='Category Image', required=False, widget=CustomImageInputCategory)
    
class ItemForm(forms.ModelForm):
    """
    Item form
    """
    class Meta:
        model = Item
        fields = '__all__'