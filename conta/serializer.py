from rest_framework import serializers
from conta.models import Contas


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contas
        fields = ['agencia', 'conta','saldo', 'get_ultima_movimentacao']

