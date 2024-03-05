from django.contrib import admin
from checkout.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Class registers Vouchers to Admin"""

    list_display = ("date", "order_number")