# PEP8
# Imports
from django.urls import path
from django.contrib.auth.decorators import login_required
from history import views


urlpatterns = [
    path(
        "",
        login_required(views.UserInvoicesView.as_view()),
        name="order-history",
    ),
    path(
        "user-invoice-view/<int:invoice_pk>/",
        login_required(views.UserViewInvoiceView.as_view()),
        name="user-invoice-view",
    ),
    path(
        "user-invoice-download/<int:invoice_pk>/",
        login_required(views.UserDownloadInvoiceView.as_view()),
        name="user-invoice-download",
    ),
]
