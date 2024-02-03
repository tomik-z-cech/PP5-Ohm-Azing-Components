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
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs.update({'placeholder': 'Enter category name (required)'})    
    
    category_image = forms.ImageField(label='Category Image', required=False, widget=CustomImageInputCategory)
    
class ItemForm(forms.ModelForm):
    """
    Item form
    """
    class Meta:
        model = Item
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['item_name'].widget.attrs.update({'placeholder': 'Enter item name (required)'})
        self.fields['item_sku'].widget.attrs.update({'placeholder': 'Enter item SKU (required)'})
        self.fields['item_description'].widget.attrs.update({'placeholder': 'Enter item description (required)'})