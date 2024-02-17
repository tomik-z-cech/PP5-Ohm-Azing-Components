# Imports
from django.shortcuts import render
from django.views import generic
from django.db.models import Count, F, ExpressionWrapper, fields, Q
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
            items = Item.objects.all().order_by('item_name').annotate(
            like=Count("item_likes"),
            dislike=Count("item_dislikes"),
            item_likes_num=ExpressionWrapper(
                F('like') - F('dislike'),
                output_field=fields.IntegerField()
                )
            ).annotate(
            item_comments_num=Count(
                "comments_num", filter=Q(item_comments__approved=1)
            )
        )
            selected_category = 'All Products'
        else:
            items = Item.objects.filter(item_category__pk=category_pk).annotate(
            like=Count("item_likes"),
            dislike=Count("item_dislikes"),
            item_likes_num=ExpressionWrapper(
                F('like') - F('dislike'),
                output_field=fields.IntegerField()
                )
            ).annotate(
            item_comments_num=Count(
                "item_comments", filter=Q(item_comments__approved=1)
            )
        )
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
