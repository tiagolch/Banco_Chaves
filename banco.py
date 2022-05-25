from datetime import date
import os
print('='*30)
print('Bem vindo ao banco Chaves')
print('='*30)


saldo = 0.0
extrato = []

def clear():
  return os.system('clear')

def add_extrato(valor):
  global extrato
  extrato.append(f'Dia - {str(date.today())} Valor {str(valor)}')



def consulta_saldo():
    # clear()
    global saldo
    print(f'Seu saldo é R${saldo}')
    #return saldo


def consulta_extrato():
    clear()
    global extrato
    print('+'*30)
    for i in extrato:
      print(i)
    consulta_saldo()
    print('+' * 30)


def deposito(valor):
    clear()
    if valor < 0:
        print(f'{valor} Não é um deposito valido')
    else:
        global saldo
        saldo += valor
        add_extrato(f'+{valor}')
        return saldo


def saque(valor):
    clear()
    global saldo
    if float(valor) <= saldo:
        saldo -= valor
        add_extrato(f'-{valor}')
    else:
        print(f'Não ha saldo suficiente, saldo atual R${saldo}')



opcao = 0
while opcao != 5:
    #print(f'Seu saldo atual é R${saldo}')
    print('O que deseja?')
    print('===============')
    print('1: Depositar')
    print('2: Sacar')
    print('3: Ver Saldo')
    print('4: Ver Extrato')
    print('5: Sair')
    print('==============')
    print('.')
    opcao = int(input('Opção => '))

    if opcao == 1:
      while True:
        try:
          valor = float(input('Qual valor para Deposito? R$'))
          if valor > 0:
            saldo = deposito(valor)
            break
        except:
          print('Only positive numbers')
          
    elif opcao == 2:
      while True:
        try:
          valor = float(input('Qual valor para Saque? R$'))
          if valor > 0:
            saque(valor)
            break
        except:
          print('Only positive numbers')
    elif opcao == 3:
        consulta_saldo()
    elif opcao == 4:
        consulta_extrato()
    else:
        print('Ate logo')





