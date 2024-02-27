def wishlist_content(request):
    """
    Method returns amount of items in wishlist
    """
    # If user is loged in
    if request.user.is_authenticated:
        # Count item in wishlist of logged in user
        items_in_wishlist = len(request.user.userprofile.user_wishlist)
    else:
        # If user is not loged in, amount = 0
        items_in_wishlist = 0
    # Context dictionary
    wishlist_context = {
        "items_in_wishlist": items_in_wishlist,
    }
    # Return context dictionary
    return wishlist_context