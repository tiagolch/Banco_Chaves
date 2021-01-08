from rest_framework import viewsets
from conta.models import Contas
from conta.serializer import ContaSerializer


class ContasViewSet(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContaSerializer
