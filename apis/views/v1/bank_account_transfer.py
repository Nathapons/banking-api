from rest_framework.viewsets import GenericViewSet, mixins

from apis.serializers import BankAccountTransferSerializer
from apis.models import BankAccountTransfer


class BankAccountTransferViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        GenericViewSet,):
    queryset = BankAccountTransfer.objects.all()
    serializer_class = BankAccountTransferSerializer
