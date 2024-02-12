# Imports
from django_resized import ResizedImageField
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model
    """
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    phone_number = models.CharField(max_length=20, blank=False, null=True)
    marketing = models.BooleanField()
    profile_picture = ResizedImageField(size=[300, 300], crop=['middle', 'center'], quality=75, upload_to="item_images/", force_format='WEBP', blank=True)
    address_1 = models.CharField(max_length=100, blank=False, null=True)
    address_2 = models.CharField(max_length=100, blank=False, null=True)
    city = models.CharField(max_length=50, blank=False, null=True)
    county = models.CharField(max_length=50, blank=False, null=True)
    post_code = models.CharField(max_length=15, blank=False, null=True)
    country = CountryField(blank=False, null=True)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return self.first_name
