# Imports
from django.contrib import messages
from django.shortcuts import render, redirect
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
        return self.request.user == UserProfile.user
    
    def get(self, request, *args, **kwargs):
        """Method generates view for profile manager"""
        # Request logged in user
        profile_selected = request.user.userprofile
        # Prepopulate form
        profile_form = UserProfileForm(instance=profile_selected)
        # Render template
        return render(
            request,
            self.template_name,
            {"profile_form": profile_form},
        )
        
    def post(self, request, *args, **kwargs):
        """
        Function triggers when submit button on my details form is pressed
        """
        profile_selected = request.user.userprofile
        profile_form = UserProfileForm(request.POST, instance=profile_selected)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile details were updated.')
        else:
            messages.error(request, "Your profile details weren't updated.")
        return redirect("profile-manager")  # Redirect back to profile manager