# PEP8
# Imports
from django.contrib import admin
from checkout.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Class registers Orders to Admin"""

    readonly_fields = [field.name for field in Order._meta.get_fields()]

    list_display = ("date", "order_number")
