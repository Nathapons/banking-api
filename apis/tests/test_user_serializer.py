from django.test import TestCase
from django.contrib.auth.models import User

from apis.tests.base import BaseTestCaseMixin
from apis.serializers import UserSerializer


class TestUserSedrializer(BaseTestCaseMixin, TestCase):

    def test_retrive(self):
        serializer = UserSerializer(self.user1)

        self.assertEqual(serializer.data['username'], 'user1')
        self.assertTrue(serializer.data['password'], self.user1.password)

    def test_list(self):
        users = [self.user1, self.user2]
        serializer = UserSerializer(users, many=True)

        self.assertEqual(len(serializer.data), len(users))

    def test_create(self):
        data = {'username': 'testuser', 'password': '12345678'}
        serializer = UserSerializer(data=data)
        is_valid = serializer.is_valid()

        self.assertTrue(is_valid)