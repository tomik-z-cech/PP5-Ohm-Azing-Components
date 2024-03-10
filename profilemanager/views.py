# PEP8
# Imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
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
        """Test function to ensure user is profile owner"""
        return self.request.user == UserProfile.user

    def get(self, request, *args, **kwargs):
        """Method generates view for profile manager"""
        # Request logged in user
        profile_selected = request.user.userprofile
        # Prepopulate form
        profile_form = UserProfileForm(instance=profile_selected)
        # If first name and last name available
        if (
            request.user.userprofile.first_name
            and request.user.userprofile.last_name
        ):
            # Get first letters
            first_letter = request.user.userprofile.first_name[0]
            second_letter = request.user.userprofile.last_name[0]
            # Set initials
            initials = first_letter + second_letter
            # Make them upper
            initials = initials.upper()
        # If only first name available
        elif (
            request.user.userprofile.first_name
            and not request.user.userprofile.last_name
        ):
            # Set the initials to only one letter
            first_letter = request.user.userprofile.first_name[0]
            second_letter = ""
            initials = first_letter + second_letter
            # Make it upper
            initials = initials.upper()
        # If only last name avaiable
        elif (
            request.user.userprofile.last_name
            and not request.user.userprofile.first_name
        ):
            # Set the initials to only one letter
            first_letter = ""
            second_letter = request.user.userprofile.last_name[0]
            initials = first_letter + second_letter
            # Make it upper
            initials = initials.upper()
        # If either first name or last name missing
        # Initials are OC (Ohm-Azing Components)
        else:
            initials = "OC"
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
        # Get the selected user profile
        profile_selected = request.user.userprofile
        # Get details from request.POST
        # Get file frem request.FILES
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=profile_selected
        )
        # If form is valid
        if profile_form.is_valid():
            # Save user profile
            profile_form.save()
            messages.success(request, "Your profile details were updated.")
        # Form not valid
        else:
            # Reset form
            profile_form = UserProfileForm()
            messages.error(request, "Your profile details weren't updated.")
        # Redirect back to profile manager
        return redirect("profile-manager")


class DeleteMyProfileView(generic.ListView):
    """
    Class deletes user profile
    """

    def get(self, request, *args, **kwargs):
        """
        Method entirely deletes user profile
        """
        # Get details of loged in user
        logged_in_user = request.user
        # Delete user profile
        logged_in_user.delete()
        # User message
        messages.info(request, "Your profile was deleted.")
        # Redirect home
        return redirect("home")
