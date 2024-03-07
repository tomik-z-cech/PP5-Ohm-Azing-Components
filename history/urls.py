# Imports
from django.urls import path
from history import views


urlpatterns = [
    path('', views.UserInvoicesView.as_view(), name='order-history'),
]