# Imports
from django.urls import path
from owner import views

urlpatterns = [
    path("", views.OwnerMainView.as_view(), name="owner"),
    path("category-delete-request/<int:category_pk>", views.DeleteCategoryView.category_delete_request, name="category-delete-request"),
    path("delete-category/<int:category_pk>/", views.DeleteCategoryView.as_view(), name="delete-category"),
    path("add-category/", views.AddCategoryView.as_view(), name="add-category"),
    path("edit-category/<int:category_pk>/", views.EditCategoryView.as_view(), name="edit-category"),
    path("items/", views.OwnerItemsView.as_view(), name="items"),
    path("item-delete-request/<int:item_pk>", views.DeleteItemView.item_delete_request, name="item-delete-request"),
    path("add-item/", views.AddItemView.as_view(), name="add-item"),
    path("edit-item/<int:item_pk>/", views.EditItemView.as_view(), name="edit-item"),
    path("delete-item/<int:item_pk>/", views.DeleteItemView.as_view(), name="delete-item"),
    path("invoices/", views.OwnerInvoicesView.as_view(), name="invoices"),
]