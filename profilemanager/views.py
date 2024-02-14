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
        return self.request.user == UserProfile.username
    
    def get(self, request, *args, **kwargs):
        """Method generates view for profile manager"""
        # Request logged in user
        login_user = request.user
        profile_selected = login_user.userprofile
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
        profile_form = UserProfileForm(request.POST)
        print(profile_form)
        #profile_form['user'] = request.user
        #if profile_form.is_valid():
        #    messages.success(request, "Your details were changed.")
        #    profile_form.save()
        #else:
        #    profile_form = UserProfileForm()
        #    messages.error(request, "Your details couldn't be changed.")
        if profile_form.is_valid():
            print('Valid')
            profile_form.save()
        else:
            for field, errors in your_form_instance.errors.items():
                print(f"Errors for {field}: {', '.join(errors)}")
        return redirect("profile-manager")  # Redirect back to profile manager