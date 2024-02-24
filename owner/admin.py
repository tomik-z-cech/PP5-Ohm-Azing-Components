from django.contrib import admin
from owner.models import Invoice, PostageSettings, Voucher, Newsletter, NewsletterEmail

# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """Class registers Invoices to Admin"""

    list_display = ("invoice_number","date_added",)

@admin.register(PostageSettings)
class PostageSettingsAdmin(admin.ModelAdmin):
    """Class registers Postage Settings to Admin"""

    list_display = ("free_postage", "standard_delivery", "express_delivery")
    
@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    """Class registers Vouchers to Admin"""

    list_display = ("voucher_code", "start_date", "end_date", "status")
    
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """Class registers Newsletter to Admin"""

    list_display = ("newsletter_email",)
    
@admin.register(NewsletterEmail)
class NewsletterEmailAdmin(admin.ModelAdmin):
    """Class registers Newsletter Emails to Admin"""

    list_display = ("subject","body")