from django.contrib import admin
from items.models import Category, Item, ItemComments

# Register your models here.
@admin.register(Category)
class CommentAdmin(admin.ModelAdmin):
    """Class registers Categories to Admin"""

    list_display = ("category_name",)
    
@admin.register(Item)
class CommentAdmin(admin.ModelAdmin):
    """Class resgisters Items to Admin"""

    list_display = ("item_name",)
    
@admin.register(ItemComments)
class StylesCommentAdmin(admin.ModelAdmin):
    """Class registers Comments to Admin"""
    list_display = ("comment_author", "comment_body", "item", "approved")
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    approve_comments.short_description = "Approve selected comments"