# PEP8
# Imports
from django.urls import path
from items import views


urlpatterns = [
    path("", views.AllItemsView.as_view(), name="all-items"),
]
