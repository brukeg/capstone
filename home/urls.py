from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_handle/', views.check_handle, name='check_handle'),
    path('register/', views.register, name='register'),
    path('check_kyc/', views.check_kyc, name='check_kyc'),
    path('request_kyc/', views.request_kyc, name='request_kyc'),
    path('link_account/', views.link_account, name='link_account'),
    path('get_accounts/', views.get_accounts, name='get_accounts'),
    path('get_transactions/', views.get_transactions, name='get_transactions'),
    path('issue_sila/', views.issue_sila, name='issue_sila'),
    path('transfer_sila/', views.transfer_sila, name='transfer_sila'),
    path('redeem_sila/', views.redeem_sila, name='redeem_sila'),
]
