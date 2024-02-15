# Imports
from django import forms
from profilemanager.models import UserProfile
from django_countries.fields import CountryField

class UserProfileForm(forms.ModelForm):
    """
    Category form
    """
    class Meta:
        model = UserProfile
        exclude = ['user', 'user_wishlist',]
        
    address_1 = forms.CharField(label='First Line of Address', required=False)
    address_2 = forms.CharField(label='Second Line of Address', required=False)
    marketing_sms = forms.BooleanField(label='Can we contact you via SMS ?', required=False)
    marketing_email = forms.BooleanField(label='Can we contact you via phone ?', required=False)
    marketing_phone = forms.BooleanField(label='Can we contact you via Email ?', required=False)
    country = forms.ChoiceField(choices=[('', 'Country')] + list(CountryField().choices), required=False)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
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
