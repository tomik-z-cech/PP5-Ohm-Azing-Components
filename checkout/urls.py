# Imports
from django.urls import path
from checkout import views
from .webhooks import webhook


urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('check-checkout-data/', views.CheckCheckoutDataView.as_view(), name='check-checkout-data'),
    path('order-success/<str:order_number>/<str:delivery_option>/', views.OrderSuccessView.as_view(), name='order-success'),
    path('wh/', webhook, name='webhook'),
]