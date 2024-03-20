from rest_framework.viewsets import ModelViewSet

from apis.serializers import BankAccountSerializer
from apis.models import BankAccount


class BankAccountViewSet(ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
