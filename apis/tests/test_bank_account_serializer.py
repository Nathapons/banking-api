from django.test import TestCase

from apis.tests.base import BaseTestCaseMixin
from apis.models import BankAccount
from apis.serializers import BankAccountSerializer


class TestBankAccountSerializer(BaseTestCaseMixin, TestCase):

    def test_retrieve(self):
        data = self.bank_account_datas[0]
        serializer_data = BankAccountSerializer(BankAccount.objects.create(**data)).data

        for key, value in data.items():
            if key == 'user_id':
                self.assertEqual(serializer_data['user'], value)
            else:
                self.assertEqual(serializer_data[key], value)

    def test_list(self):
        serializer = BankAccountSerializer(self.bank_accounts, many=True)

        self.assertEqual(len(serializer.data), len(self.bank_account_datas))

    def test_create(self):
        data = {'user': self.user1.id, 'account_no': '1234', 'balance': 30000}
        serializer = BankAccountSerializer(data=data)
        is_raise = serializer.is_valid()
        serializer.save()

        self.assertTrue(is_raise)
        for key, value in data.items():
            if key == 'user_id':
                self.assertEqual(serializer.data['user'], value)
            else:
                self.assertEqual(serializer.data[key], value)

    def test_update(self):
        data = {'balance': 11111}
        serializer = BankAccountSerializer(self.bank_accounts[0], data=data, partial=True)
        is_raise = serializer.is_valid()
        serializer.save()

        self.assertTrue(is_raise)
        self.assertEqual(serializer.data['balance'], data['balance'])
