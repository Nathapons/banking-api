from rest_framework import serializers
from django.contrib.auth.models import User

from apis.models import BankAccount, BankAccountTransfer


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data['password']
        user.set_password(password)
        return user

    class Meta:
        model = User
        fields = '__all__'


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = '__all__'


class BankAccountTransferSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)

        sender_account = attrs['sender_account']
        receiver_account = attrs['receiver_account']

        if sender_account == receiver_account:
            raise serializers.ValidationError({'message': 'Sender account is same with receiver account'})

        amount = attrs['amount']
        if sender_account.balance < amount:
            raise serializers.ValidationError({'message': 'Cannot transfer amount'})

        return attrs

    def create(self, validated_data):
        bank_account_transfer = super().create(validated_data)

        amount = validated_data['amount']
        sender_account = bank_account_transfer.sender_account
        sender_account.balance = sender_account.balance - amount
        sender_account.save()

        receiver_account = bank_account_transfer.receiver_account
        receiver_account.balance = receiver_account.balance + amount
        receiver_account.save()

        return bank_account_transfer

    class Meta:
        model = BankAccountTransfer
        fields = '__all__'
