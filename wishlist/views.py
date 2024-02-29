from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from items.models import Item

# Create your views here.
class WishlistView(LoginRequiredMixin, generic.ListView):
    
    template_name = "wishlist/wishlist.html"  # Template
    
    def wishlist_toggle(request, item_pk, *args, **kwargs):
            """
            Function is called when wishlist button pressed submitted
            """
            users_wishlist = request.user.userprofile.user_wishlist
            item_to_toggle = get_object_or_404(Item, pk=item_pk)
            if item_to_toggle.item_sku in users_wishlist:
                users_wishlist.remove(item_to_toggle.item_sku)
                messages.success(request, f'Item {item_to_toggle.item_name} was removed from your wishlist.')
            else:
                users_wishlist.append(item_to_toggle.item_sku)
                messages.success(request, f'Item {item_to_toggle.item_name} was added to your wishlist.')
            request.user.userprofile.save()
            return redirect('item-detail', item_pk=item_pk)
        
    def get(self, request, *args, **kwargs):
        user_wishlist = request.user.userprofile.user_wishlist
        wishlist_for_template = Item.objects.filter(item_sku__in=user_wishlist)
        return render(
            request,
            self.template_name,
            {
                "user_wishlist": wishlist_for_template
            },
        )
        
class ClearWishlistView(LoginRequiredMixin, generic.ListView):
    
    def get(self, request, *args, **kwargs):
        request.user.userprofile.user_wishlist = []
        request.user.userprofile.save()
        messages.success(request, f'Your wishlist is now empty.')
        return redirect("show-wishlist")  # Redirect back to Wishlist
    
    
class DeleteWishlistItemView(LoginRequiredMixin, generic.ListView):
    
    def get(self, request, item_pk, *args, **kwargs):
        item_to_delete = get_object_or_404(Item, pk=item_pk)
        users_wishlist = request.user.userprofile.user_wishlist
        users_wishlist.remove(item_to_delete.item_sku)
        request.user.userprofile.save()
        return redirect("show-wishlist")