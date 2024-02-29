# Imports
from django.urls import path
from vault import views


urlpatterns = [
    path('', views.DisplayVaultItemsView.as_view(), name='vault'),
    path('add-to-vault/<int:item_pk>/', views.add_to_vault, name='add-to-vault'),
]