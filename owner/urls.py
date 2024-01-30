# Imports
from django.urls import path
from owner import views

urlpatterns = [
    path("", views.OwnerMainView.as_view(), name="owner"),
]