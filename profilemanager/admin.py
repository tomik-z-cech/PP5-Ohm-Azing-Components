# Imports
from django.contrib import admin
from django.contrib.auth.models import User
from profilemanager.models import UserProfile


# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class ProfileAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)
    list_display = (
        "username",
        "email",
    )

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
