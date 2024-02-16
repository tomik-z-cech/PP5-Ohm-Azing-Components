# Imports
from django.shortcuts import render
from django.views import generic
from items.models import Category, Item


class AllItemsView(generic.ListView):
    """
    Class generates view of items page
    """

    template_name = "items/all_items.html"

    def get(self, request, *args, **kwargs):
        """This method generates view of items page"""
        all_categories = Category.objects.all().order_by('category_name')
        items = Item.objects.all().order_by('item_name')
        # Render template
        return render(
            request,
            self.template_name,
            {
                "all_categories": all_categories,
                "items": items,
            },
        )
