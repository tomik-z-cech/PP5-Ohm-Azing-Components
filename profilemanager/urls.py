# PEP8
# Imports
from django.urls import path
from profilemanager import views

urlpatterns = [
    path("", views.MyDetailsView.as_view(), name="profile-manager"),
    path(
        "deleteprofile/",
        views.DeleteMyProfileView.as_view(),
        name="delete-profile",
    ),
]
