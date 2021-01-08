from django.contrib import admin
from .models import Contas


@admin.register(Contas)
class ContasAdmin(admin.ModelAdmin):
    list_display = ['agencia', 'conta', 'saldo', 'get_ultima_movimentacao']
