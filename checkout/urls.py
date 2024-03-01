# Imports
from django.urls import path
from checkout import views


urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
]