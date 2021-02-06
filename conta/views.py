from rest_framework import viewsets
from conta.models import Contas, Deposito, Saque
from conta.serializer import ContaSerializer, DepositoSerializer, SaqueSerializer


class ContasViewSet(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContaSerializer


class DepositoViewSet(viewsets.ModelViewSet):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer


class SaqueViewSet(viewsets.ModelViewSet):
    queryset = Saque.objects.all()
    serializer_class = SaqueSerializer
