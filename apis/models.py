from django.db import models
from django.contrib.auth.models import User


class BankAccount(models.Model):
    account_no = models.CharField(max_length=20, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bank_account')
    balance = models.FloatField(default=0)

    class Meta:
        verbose_name = 'bank_account'
        verbose_name_plural = verbose_name


class BankAccountTransfer(models.Model):
    sender_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='sender_bank_account_transfer')
    receiver_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='receiver_bank_account_transfer')
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'bank_account_transfer'
        verbose_name_plural = verbose_name
