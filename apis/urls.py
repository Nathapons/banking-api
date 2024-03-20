from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.v1 import user, bank_account, \
    bank_account_transfer

router = DefaultRouter()
router.register(r'user', user.UserViewSet, basename='user')
router.register(r'bank-account-transfer',
                bank_account_transfer.BankAccountTransferViewSet,
                basename='bank_account_transfer')
router.register(r'bank-account',
                bank_account.BankAccountViewSet,
                basename='bank_account')

urlpatterns = [
    path('', include(router.urls)),
]
