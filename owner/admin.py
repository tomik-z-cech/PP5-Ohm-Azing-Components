from django.contrib import admin
from owner.models import Invoice, PostageSettings

# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """Class registers Invoices to Admin"""

    list_display = ("invoice_number","date_added",)

@admin.register(PostageSettings)
class PostageSettingsAdmin(admin.ModelAdmin):
    """Class registers Postage Settings to Admin"""

    list_display = ("free_postage", "standard_delivery", "express_delivery")