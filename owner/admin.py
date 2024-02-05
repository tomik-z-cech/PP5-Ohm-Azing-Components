from django.contrib import admin
from owner.models import Invoice

# Register your models here.
@admin.register(Invoice)
class CommentAdmin(admin.ModelAdmin):
    """Class registers Invoices to Admin"""

    list_display = ("invoice_number","date_added",)
