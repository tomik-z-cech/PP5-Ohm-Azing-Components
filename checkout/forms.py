# Imports
from django import forms
from checkout.models import Order
from django_countries.fields import CountryField

class OrderForm(forms.ModelForm):
    """
    Category form
    """
    
    DELIVERY_OPTIONS = ((0, "Standard Delivery"), (1, "Express Delivery"))
    
    class Meta:
        model = Order
        exclude = ['order_number', 'user', 'delivery_cost', 'sub_total', 'vat', 'total', 'original_vault', 'stripe_pid', 'invoice']
        
    address_1 = forms.CharField(label='First Line of Address', required=False)
    address_2 = forms.CharField(label='Second Line of Address', required=False)
    country = forms.ChoiceField(choices=[('', 'Country')] + list(CountryField().choices), required=False)
    delivery_option = forms.ChoiceField(widget=forms.RadioSelect, choices=DELIVERY_OPTIONS, initial=0)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        fields_to_add_class = self.fields.keys()
        for field in fields_to_add_class:
            self.fields[field].widget.attrs.update({
                'class': 'shadow-none',
            })
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Your First Name(s)'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Your Last Name'})
        self.fields['address_1'].widget.attrs.update({'placeholder': 'First Line of Address'})
        self.fields['address_2'].widget.attrs.update({'placeholder': 'Second Line of Address'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City'})
        self.fields['county'].widget.attrs.update({'placeholder': 'County'})
        self.fields['post_code'].widget.attrs.update({'placeholder': 'Post Code (Eir Code)'})
        self.fields['voucher'].widget.attrs.update({'placeholder': 'Discount Code'})
        self.fields['voucher'].label = ''
        