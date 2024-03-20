from django.test import TestCase

from apis.tests.base import BaseTestCaseMixin
from apis.models import BankAccountTransfer
from apis.serializers import BankAccountTransferSerializer


class TestBankAccountTransferSerializer(BaseTestCaseMixin, TestCase):

    def setUp(self):
        super().setUp()

        [sender_account, receiver_account] = self.bank_accounts
        self.datas = [
            {'sender_account': sender_account.id, 'receiver_account': receiver_account.id, 'amount': 700},
            {'sender_account': sender_account.id, 'receiver_account': receiver_account.id, 'amount': 800}
        ]

    def test_create(self):
        [sender_account, receiver_account] = self.bank_accounts
        data = {'sender_account': sender_account.id, 'receiver_account': receiver_account.id, 'amount': 700}
        serializer = BankAccountTransferSerializer(data=data)
        is_valid = serializer.is_valid()
        serializer.save()

        self.assertTrue(is_valid)
        self.assertEqual(serializer.data['sender_account'], sender_account.id)
        self.assertEqual(serializer.data['receiver_account'], receiver_account.id)
        self.assertEqual(serializer.data['amount'], data['amount'])

        data = {'sender_account': sender_account.id, 'receiver_account': sender_account.id, 'amount': 10}
        serializer = BankAccountTransferSerializer(data=data)
        is_valid = serializer.is_valid()
        err_message =  str(serializer.errors['message'][0])
        self.assertFalse(is_valid)
        self.assertEqual(err_message, 'Sender account is same with receiver account')

        data = {'sender_account': sender_account.id, 'receiver_account': receiver_account.id, 'amount': 99999999}
        serializer = BankAccountTransferSerializer(data=data)
        is_valid = serializer.is_valid()
        err_message =  str(serializer.errors['message'][0])
        self.assertFalse(is_valid)
        self.assertEqual(err_message, 'Cannot transfer amount')
        

    def test_retrieve(self):
        [sender_account, receiver_account] = self.bank_accounts
        data = {'sender_account_id': sender_account.id, 'receiver_account_id': receiver_account.id, 'amount': 700}
        bank_account = BankAccountTransfer.objects.create(**data)
        serializer = BankAccountTransferSerializer(bank_account)

        self.assertEqual(serializer.data['sender_account'], sender_account.id)
        self.assertEqual(serializer.data['receiver_account'], receiver_account.id)
        self.assertEqual(serializer.data['amount'], data['amount'])

    def test_list(self):
        bank_accounts = [
            BankAccountTransfer.objects.create(
                sender_account_id=data['sender_account'],
                receiver_account_id=data['receiver_account'],
                amount=data['amount']
            ) 
            for data in self.datas
        ]
        serializer_datas = BankAccountTransferSerializer(bank_accounts, many=True).data

        self.assertEqual(len(serializer_datas), len(bank_accounts))
