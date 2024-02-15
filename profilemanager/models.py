# Imports
from django_resized import ResizedImageField
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField



class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile', null=False)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    marketing_phone = models.BooleanField(default=True)
    marketing_email = models.BooleanField(default=True)
    marketing_sms = models.BooleanField(default=True)
    profile_picture = ResizedImageField(size=[300, 300], quality=75, upload_to="profile_pictures/", force_format='WEBP', blank=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=15, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    user_wishlist = ArrayField(models.CharField(max_length=254), blank=True, null=True)


    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update the user profile
        """
        if created:
            UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.userprofile.save()