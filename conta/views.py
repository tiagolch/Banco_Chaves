from rest_framework import viewsets
from conta.models import Contas, Deposito
from conta.serializer import ContaSerializer, DepositoSerializer


class ContasViewSet(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContaSerializer


class DepositoViewSet(viewsets.ModelViewSet):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer
