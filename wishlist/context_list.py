def wishlist_content(request):
    if request.user.is_authenticated:
        items_in_wishlist = len(request.user.userprofile.user_wishlist)
    else:
        items_in_wishlist = 0
    wishlist_context = {
        "items_in_wishlist": items_in_wishlist,
    }
    return wishlist_context