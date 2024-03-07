# PEP8
# Imports
from django.urls import path
from landing import views


urlpatterns = [
    path("", views.LandingPageView.as_view(), name="home"),
    path("search", views.SearchView.as_view(), name="search"),
]
