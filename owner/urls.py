# Imports
from django.urls import path
from django.contrib.auth.decorators import login_required
from owner import views

urlpatterns = [
    path("", login_required(views.OwnerMainView.as_view()), name="owner"),
    path("category-delete-request/<int:category_pk>", login_required(views.DeleteCategoryView.category_delete_request), name="category-delete-request"),
    path("delete-category/<int:category_pk>/", login_required(views.DeleteCategoryView.as_view()), name="delete-category"),
    path("add-category/", login_required(views.AddCategoryView.as_view()), name="add-category"),
    path("edit-category/<int:category_pk>/", login_required(views.EditCategoryView.as_view()), name="edit-category"),
    path("items/", login_required(views.OwnerItemsView.as_view()), name="items"),
    path("item-delete-request/<int:item_pk>", login_required(views.DeleteItemView.item_delete_request), name="item-delete-request"),
    path("add-item/", login_required(views.AddItemView.as_view()), name="add-item"),
    path("edit-item/<int:item_pk>/", login_required(views.EditItemView.as_view()), name="edit-item"),
    path("delete-item/<int:item_pk>/", login_required(views.DeleteItemView.as_view()), name="delete-item"),
    path("invoices/", login_required(views.OwnerInvoicesView.as_view()), name="invoices"),
    path("download-invoice/<int:invoice_pk>/", login_required(views.DownloadInvoiceView.as_view()), name="download-invoice"),
    path("postage-settings/", login_required(views.PostageSettingsView.as_view()), name="postage-settings"),
    path("comments/", login_required(views.CommentsOwnerView.as_view()), name="comments-owner"),
    path("comment-delete-request/<int:comment_pk>", login_required(views.DeleteCommentView.comment_delete_request), name="comment-delete-request"),
    path("delete-comment/<int:comment_pk>/", login_required(views.DeleteCommentView.as_view()), name="delete-comment"),
    path("approve-comment/<int:comment_pk>/", login_required(views.ApproveCommentView.as_view()), name="approve-comment"),
    path("vouchers/", login_required(views.VouchersOwnerView.as_view()), name="vouchers-owner"),
    path("add-voucher/", login_required(views.AddVoucherView.as_view()), name="add-voucher"),
    path("voucher-delete-request/<int:voucher_pk>", login_required(views.DeleteVoucherView.voucher_delete_request), name="voucher-delete-request"),
    path("delete-voucher/<int:voucher_pk>/", login_required(views.DeleteVoucherView.as_view()), name="delete-voucher"),
    path("edit-voucher/<int:voucher_pk>/", login_required(views.EditVoucherView.as_view()), name="edit-voucher"),
    path("emails/", login_required(views.EmailsOwnerView.as_view()), name="emails-owner"),
    path("new-email/", login_required(views.NewEmailView.as_view()), name="new-email"),
]