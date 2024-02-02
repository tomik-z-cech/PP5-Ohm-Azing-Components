from django.contrib import admin
from items.models import Category, Item

# Register your models here.
@admin.register(Category)
class CommentAdmin(admin.ModelAdmin):
    """Class resgisters Categories to Admin"""

    list_display = ("category_name",)
    
@admin.register(Item)
class CommentAdmin(admin.ModelAdmin):
    """Class resgisters Items to Admin"""

    list_display = ("item_name",)