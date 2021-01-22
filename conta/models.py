from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contas(models.Model):
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=6)
    saldo = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    ultima_movimentacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.agencia)}/{str(self.conta)}'

    def get_ultima_movimentacao(self):
        return self.ultima_movimentacao.strftime('%d/%m/%Y %H:%M')


class Deposito(models.Model):
    conta = models.ForeignKey('Contas', on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    data_deposito = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.conta)}'

    def get_data_deposito(self):
        return self.data_deposito.strftime('%d/%m/%Y %H:%M')


@receiver(post_save, sender=Deposito)
def update_saldo(sender, instance, **kwargs):
    instance.conta.saldo += instance.valor
    instance.conta.save()