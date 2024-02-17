# PEP8
# Imports
from django.urls import path
from items import views


urlpatterns = [
    path("<int:category_pk>/", views.ShopView.as_view(), name="shop"),
]