from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from items.models import Item

# Create your views here.
class WishlistView(generic.ListView):
    @login_required    
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