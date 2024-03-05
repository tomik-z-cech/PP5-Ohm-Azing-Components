# Imports
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.widgets import CKEditorWidget
from owner.widgets import CustomImageInputCategory, CustomImageInputItem1, CustomImageInputItem2, CustomImageInputItem3
from items.models import Category, Item
from owner.models import PostageSettings, Voucher, Newsletter, NewsletterEmail

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
        exclude = ['item_dislikes', 'item_likes', 'date_added']
        
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
    
    
class PostageSettingsForm(forms.ModelForm):
    """
    Postage form
    """
    class Meta:
        model = PostageSettings
        fields = ("__all__")
        
    def __init__(self, *args, **kwargs):
        super(PostageSettingsForm, self).__init__(*args, **kwargs)
        fields_to_add_class = self.fields.keys()
        for field in fields_to_add_class:
            self.fields[field].widget.attrs.update({
                'class': 'shadow-none',
            })
        self.fields['free_postage'].widget.attrs.update({
            'placeholder': 'Free postage threshold € (required)',
            'step': '0.05',
            'min': '1',
        })
        self.fields['standard_delivery'].widget.attrs.update({
            'placeholder': 'Postage cost % (required)',
            'step': '0.05',
            'min': '1',
        })
        self.fields['express_delivery'].widget.attrs.update({
            'placeholder': 'Postage cost % (required)',
            'step': '0.05',
            'min': '1',
        })
        self.fields['minimum_order'].widget.attrs.update({
            'placeholder': 'Minimum order € (required)',
            'step': '1',
            'min': '1',
        })
        
class VoucherForm(forms.ModelForm):
    """
    Voucher form
    """
    class Meta:
        model = Voucher
        fields = ('__all__')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super(VoucherForm, self).__init__(*args, **kwargs)
        fields_to_add_class = self.fields.keys()
        for field in fields_to_add_class:
            self.fields[field].widget.attrs.update({
                'class': 'shadow-none',
            })
        self.fields['discount'].widget.attrs.update({
            'placeholder': 'Enter % of discount',
            'step': '1',
            'min': '1',
            'max': '100',
        })
        self.fields['voucher_code'].widget.attrs.update({
            'placeholder': 'Enter CODE of discount',
        })
            
    discount = forms.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )
    

class NewsletterForm(forms.ModelForm):
    """
    Newsletter form
    """
    class Meta:
        model = Newsletter
        fields = ('__all__')
        widgets = {
            'newsletter_email': forms.DateInput(attrs={'type': 'email', 'placeholder':'your@email.ie'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        fields_to_add_class = self.fields.keys()
        for field in fields_to_add_class:
            self.fields[field].widget.attrs.update({
                'class': 'shadow-none',
            })
            
class NewsletterEmailForm(forms.ModelForm):
    """
    Newsletter Emails form
    """
    class Meta:
        model = NewsletterEmail
        fields = ('subject', 'body')
        
        body = forms.CharField(widget=CKEditorWidget())
        
    def __init__(self, *args, **kwargs):
        super(NewsletterEmailForm, self).__init__(*args, **kwargs)
        fields_to_add_class = self.fields.keys()
        for field in fields_to_add_class:
            self.fields[field].widget.attrs.update({
                'class': 'shadow-none',
            })
            
    