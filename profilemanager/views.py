# Imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
# Views security
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from .models import User
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
        # Initials to display if no profile picture available
        if request.user.userprofile.first_name and request.user.userprofile.last_name:
            first_letter = request.user.userprofile.first_name[0]
            second_letter = request.user.userprofile.last_name[0]
            initials = first_letter + second_letter
            initials = initials.upper()
        elif request.user.userprofile.first_name and not request.user.userprofile.last_name:
            first_letter = request.user.userprofile.first_name[0]
            second_letter = ""
            initials = first_letter + second_letter
            initials = initials.upper()
        elif request.user.userprofile.last_name and not request.user.userprofile.first_name:
            first_letter = ""
            second_letter = request.user.userprofile.last_name[0]
            initials = first_letter + second_letter
            initials = initials.upper()
        else:
            initials = 'OC'
        # Render template
        return render(
            request,
            self.template_name,
            {
            "profile_form": profile_form,
            "profile_picture": profile_selected.profile_picture,
            "initials": initials,
            },
        )
        
    def post(self, request, *args, **kwargs):
        """
        Function triggers when submit button on my details form is pressed
        """
        profile_selected = request.user.userprofile
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile_selected)
        print(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile details were updated.')
        else:
            messages.error(request, "Your profile details weren't updated.")
        return redirect("profile-manager")  # Redirect back to profile manager
    
    
class DeleteMyProfileView(generic.ListView):
    """
    Class deletes user profile
    """
    def get(self, request, *args, **kwargs):
        """Method entirely deletes user profile"""
        logged_in_user = request.user
        # Delete user profile
        logged_in_user.delete()
        # User message
        messages.info(request, 'Your profile was deleted.')
        # Redirect home
        return redirect("home")
