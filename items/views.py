# Imports
from django.shortcuts import render
from django.views import generic
from items.models import Category, Item


class ShopView(generic.ListView):
    """
    Class generates view of items page
    """

    template_name = "items/shop.html"

    def get(self, request, category_pk, *args, **kwargs):
        """This method generates view of items page"""
        all_categories = Category.objects.all().order_by('category_name')
        if category_pk == 0:
            items = Item.objects.all().order_by('item_name')
            selected_category = 'All Products'
        else:
            items = Item.objects.filter(item_category__pk=category_pk)
            running_category = Category.objects.filter(pk=category_pk).first()
            selected_category = running_category.category_name
        # Render template
        return render(
            request,
            self.template_name,
            {
                "all_categories": all_categories,
                "items": items,
                "selected_category": selected_category,
            },
        )
