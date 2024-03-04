# Imports
from django.urls import path
from checkout import views
from .webhooks import webhook


urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('check-checkout-data/', views.CheckCheckoutDataView.as_view(), name='check-checkout-data'),
    path('wh/', webhook, name='webhook'),
]