from django.contrib import admin

from apis.models import BankAccount, BankAccountTransfer


class BankAccountAdmin(admin.ModelAdmin):
    list_display = [
        'account_no',
        'user',
        'balance',
    ]


class BankAccountTransferAdmin(admin.ModelAdmin):
    list_display = [
        'sender_account',
        'receiver_account',
        'amount',
        'created_at',
    ]


admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(BankAccountTransfer, BankAccountTransferAdmin)
