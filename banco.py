from datetime import date
print('='*30)
print('Bem vindo ao banco Chaves')
print('='*30)


saldo = 0.0
extrato = []


def consulta_saldo():
    global saldo
    print(f'Seu saldo é R${saldo}')
    #return saldo


def consulta_extrato():
    global extrato
    print('+'*30)
    for i in extrato:
        print(i)
    print('+' * 30)


def deposito(x):
    if x < 0:
        print(f'{x} Não é um deposito valido')
    else:
        global saldo
        saldo += x
        extrato.append(f'Dia - {str(date.today())} Valor +{str(valor)} -- Saldo {str(saldo)}')
        return saldo


def saque(valor):
    global saldo
    global extrato
    if int(valor) <= saldo:
        saldo -= valor
        extrato.append(f'Dia - {str(date.today())} Valor -{str(valor)} -- Saldo {str(saldo)}')
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
        valor = float(input('Qual valor para Deposito? R$'))
        saldo = deposito(valor)

    elif opcao == 2:
        valor = float(input('Qual valor para Saque? R$'))
        saque(valor)

    elif opcao == 3:
        consulta_saldo()
    elif opcao == 4:
        consulta_extrato()
    else:
        print('Ate logo')






