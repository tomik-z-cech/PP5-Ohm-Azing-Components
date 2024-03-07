from django.contrib import admin
from owner.models import PostageSettings, Voucher, Newsletter, NewsletterEmail

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