from django.contrib import admin
from products.models import Category

# Register your models here.
@admin.register(Category)
class CommentAdmin(admin.ModelAdmin):
    """Class resgisters Categories to Admin"""

    list_display = ("category_name",)