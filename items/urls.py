# PEP8
# Imports
from django.urls import path
from django.contrib.auth.decorators import login_required
from items import views


urlpatterns = [
    path("<int:category_pk>/", views.ShopView.as_view(), name="shop"),
    path(
        "item-detail/<int:item_pk>/",
        views.ItemDetailView.as_view(),
        name="item-detail",
    ),
    path(
        "submit-comment/<int:item_pk>/",
        login_required(views.ItemDetailView.submit_comment),
        name="submit-comment",
    ),
    path(
        "item-like/<int:item_pk>/",
        login_required(views.ItemLikeView.as_view()),
        name="item-like",
    ),
    path(
        "item-dislike/<int:item_pk>/",
        login_required(views.ItemDislikeView.as_view()),
        name="item-dislike",
    ),
]
