from django.contrib.auth.models import User
from apis.models import BankAccount


class BaseTestCaseMixin:

    def setUp(self):
        self.user1 = User.objects.create(username="user1")
        self.user1.set_password('1234')
        self.user1.save()
        self.user2 = User.objects.create(username="user2")
        self.user2.set_password('1234')
        self.user2.save()

        self.bank_account_datas = [
            {'user_id': self.user1.id, 'account_no': '1234', 'balance': 30000},
            {'user_id': self.user2.id, 'account_no': '5678', 'balance': 300}
        ]
        self.bank_accounts = [BankAccount.objects.create(**data) for data in self.bank_account_datas]
