# Imports
from django.contrib import messages
from django.shortcuts import render
from django.views import generic
# Views security
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from profilemanager.models import UserProfile
from profilemanager.forms import UserProfileForm

class MyDetailsView(generic.ListView, UserPassesTestMixin, LoginRequiredMixin):
    """
    Class generates view for user profile details
    """
    
    template_name = "profilemanager/my_details.html"
    model = UserProfile

    def test_func(self):
        """Test function to ensure user is superuser"""
        return self.request.user == UserProfile.username
    
    def get(self, request, *args, **kwargs):
        """Method generates view for profile manager"""
        # Request logged in user
        login_user = request.user
        print(login_user)
        # profile_selected = UserProfile.user.login_user.userprofile
        # Prepopulate form
        profile_form = UserProfileForm(instance=login_user)
        # Render template
        return render(
            request,
            self.template_name,
            {"profile_form": profile_form},
        )