from rest_framework import serializers
from conta.models import Contas, Deposito, Saque


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contas
        fields = ['agencia', 'conta', 'saldo', 'get_ultima_movimentacao']


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ['id', 'conta', 'valor', 'get_data_deposito']


class SaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saque
        fields = ['id', 'conta', 'valor', 'get_data_saque']