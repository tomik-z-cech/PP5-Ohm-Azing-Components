# Imports
import uuid
from django.db import models
from django_countries.fields import CountryField
from profilemanager.models import UserProfile

# Create your models here.
class Order(models.Model):
    
    
    
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    address_1 = models.CharField(max_length=100, blank=False, null=False)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    county = models.CharField(max_length=50, blank=False, null=False)
    post_code = models.CharField(max_length=15, blank=False, null=False)
    country = CountryField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_option = models.IntegerField()
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    voucher = models.CharField(max_length=20, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_vault = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    invoice = models.FileField(upload_to='invoices/')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

