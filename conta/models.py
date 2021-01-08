from django.db import models


class Contas(models.Model):
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=6)
    saldo = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    ultima_movimentacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.conta

    def get_ultima_movimentacao(self):
        return self.ultima_movimentacao.strftime('%d/%m/%Y %H:%M')