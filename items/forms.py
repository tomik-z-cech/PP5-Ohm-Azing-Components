# Imports
from django import forms
from django.core.validators import MinValueValidator
from owner.widgets import CustomImageInputCategory, CustomImageInputItem1, CustomImageInputItem2, CustomImageInputItem3
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
        self.fields['category_name'].widget.attrs.update({
            'placeholder': 'Enter category name (required)',
            'class': 'shadow-none',
        })
            
    
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
        fields_to_add_class = self.fields.keys()
        for field in fields_to_add_class:
            self.fields[field].widget.attrs.update({
                'class': 'shadow-none',
            })
        self.fields['item_name'].widget.attrs.update({'placeholder': 'Enter item name (required)'})
        self.fields['item_sku'].widget.attrs.update({'placeholder': 'Enter item SKU (required)'})
        self.fields['price_per_unit'].widget.attrs.update({
            'placeholder': 'Enter price per unit (required)',
            'step': '0.05',
            'min': '0',
        })
        self.fields['price_per_unit'].validators.append(MinValueValidator(0))
        self.fields['item_description'].widget.attrs.update({
            'placeholder': 'Enter item description (required)',
            'rows': 3,
        })
        self.fields['item_stock'].widget.attrs.update({
            'placeholder': 'Enter current stock amount',
            'step': '1',
            'min': '0',
        })
        
    image_1 = forms.ImageField(label='Image 1', required=False, widget=CustomImageInputItem1)
    image_2 = forms.ImageField(label='Image 2', required=False, widget=CustomImageInputItem2)
    image_3 = forms.ImageField(label='Image 3', required=False, widget=CustomImageInputItem3)
    
    
class PageSortFormAdmin(forms.Form):
    LENGTH_CHOICES = [(5, '5 items per page'), (10, '10 items per page'), (20, '20 items per page'), (-1, 'All items')]
    length = forms.ChoiceField(choices=LENGTH_CHOICES, initial=5)
    SORT_CHOICES = [(0, 'Name A-Z'), (1, 'Name Z-A'), (2, 'Price Low - High'), (3, 'Price High - Low'), (4, 'Stock Low - High'),(5, 'Stock High - Low '), (6, 'Most liked'), (7, 'Least liked')]
    sort = forms.ChoiceField(choices=SORT_CHOICES, initial=0)
