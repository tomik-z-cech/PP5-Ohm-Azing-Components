# PEP8
# Imports
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from items.models import Item


class WishlistView(LoginRequiredMixin, generic.ListView):
    """
    Class for managing wishlist
    """

    template_name = "wishlist/wishlist.html"

    def wishlist_toggle(request, item_pk, *args, **kwargs):
        """
        Function is called when wishlist button pressed
        """
        # Get current users wishlist
        users_wishlist = request.user.userprofile.user_wishlist
        # Get item that requested the toggle
        item_to_toggle = get_object_or_404(Item, pk=item_pk)
        # If item already in wishlist
        if item_to_toggle.item_sku in users_wishlist:
            # Remove item from wishlist
            users_wishlist.remove(item_to_toggle.item_sku)
            messages.success(
                request,
                f"{item_to_toggle.item_name} removed from your wishlist.",
            )
        # If item not in wishlist yet
        else:
            # Add item to wishlist
            users_wishlist.append(item_to_toggle.item_sku)
            messages.success(
                request,
                f"Item {item_to_toggle.item_name} was added to your wishlist.",
            )
        # Save the wishlist to user profile
        request.user.userprofile.save()
        # Redirect back to item detial
        return redirect("item-detail", item_pk=item_pk)

    def get(self, request, *args, **kwargs):
        """
        Method displays content of wishlist
        """
        # Get users wishlist content
        user_wishlist = request.user.userprofile.user_wishlist
        # Translate wishlist for template using item sku
        wishlist_for_template = Item.objects.filter(item_sku__in=user_wishlist)
        # Render template
        return render(
            request,
            self.template_name,
            {"user_wishlist": wishlist_for_template},
        )


class ClearWishlistView(LoginRequiredMixin, generic.ListView):
    """
    Class clears content of users wishlist
    """

    def get(self, request, *args, **kwargs):
        """
        Method clears user wishlist content
        """
        # Set user wishlist to empty array
        request.user.userprofile.user_wishlist = []
        # Save the wishlist
        request.user.userprofile.save()
        messages.success(request, f"Your wishlist is now empty.")
        # Redirect back to wishlist
        return redirect("show-wishlist")


class DeleteWishlistItemView(LoginRequiredMixin, generic.ListView):
    """
    Class deletes item from wishlist
    """

    def get(self, request, item_pk, *args, **kwargs):
        """
        Method deletes item from wishlist
        """
        # Get requested item
        item_to_delete = get_object_or_404(Item, pk=item_pk)
        # Request current users wishlist
        users_wishlist = request.user.userprofile.user_wishlist
        # Remove requested item from users wishlist
        users_wishlist.remove(item_to_delete.item_sku)
        # Save wishlist
        request.user.userprofile.save()
        # Return back to wishlist
        return redirect("show-wishlist")
