# Imports
from django.urls import path
from owner import views

urlpatterns = [
    path("", views.OwnerMainView.as_view(), name="owner"),
    path("category-delete-request/<int:category_pk>", views.DeleteCategoryView.category_delete_request, name="category-delete-request"),
    path("delete-category/<int:category_pk>/", views.DeleteCategoryView.as_view(), name="delete-category"),
    path("add-category/", views.CreateCategoryView.as_view(), name="add-category"),
    path("edit-category/<int:category_pk>/", views.EditCategoryView.as_view(), name="edit-category"),
    path("items/", views.OwnerItemsView.as_view(), name="items"),
]