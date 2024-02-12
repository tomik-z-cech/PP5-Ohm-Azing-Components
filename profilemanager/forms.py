# Imports
from django import forms
from profilemanager.models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    Category form
    """
    class Meta:
        model = UserProfile
        fields = '__all__'
    