from rest_framework import serializers
from conta.models import Contas, Deposito


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contas
        fields = ['agencia', 'conta','saldo', 'get_ultima_movimentacao']


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ['id', 'conta', 'valor', 'get_data_deposito']