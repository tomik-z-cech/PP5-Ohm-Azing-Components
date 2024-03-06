# Imports
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=15, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_option = models.IntegerField()
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    voucher = models.CharField(max_length=30, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_vault = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    invoice = models.FileField(upload_to='media/invoices')
    
    def __str__(self):
        return self.order_number

