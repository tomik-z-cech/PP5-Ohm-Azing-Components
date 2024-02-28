# Imports
from django.urls import path
from django.contrib.auth.decorators import login_required
from wishlist import views


urlpatterns = [
    path('', login_required(views.WishlistView.as_view()), name='show-wishlist'),
    path('wishlist-toggle/<int:item_pk>/', login_required(views.WishlistView.wishlist_toggle), name='wishlist-toggle'),
]