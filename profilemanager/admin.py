# PEP8
# Imports
from django.contrib import admin
from django.contrib.auth.models import User
from profilemanager.models import UserProfile


# Register your models here.
class UserProfileInline(admin.StackedInline):
    """
    Class registers UserProfile inline with User model
    """

    model = UserProfile
    can_delete = False


class ProfileAdmin(admin.ModelAdmin):
    """
    Class registers UserProfile into admin
    """

    inlines = (UserProfileInline,)
    list_display = (
        "username",
        "email",
    )


# Unregister User
admin.site.unregister(User)
# Register User inline with ProfileAdmin class
admin.site.register(User, ProfileAdmin)
