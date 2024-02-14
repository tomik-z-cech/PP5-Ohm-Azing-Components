# Imports
from django import forms
from profilemanager.models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    Category form
    """
    class Meta:
        model = UserProfile
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        fields_to_add_class = self.fields.keys()
        for field in fields_to_add_class:
            self.fields[field].widget.attrs.update({
                'class': 'shadow-none',
            })
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Your First Name(s)'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Your Last Name'})
    