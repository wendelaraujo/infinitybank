from banco import *
from operacoes.transferencia import transferir
from operacoes.saque import sacar
from operacoes.consulta import consultarSaldo
from operacoes.deposito import depositar

def menu():
    while True:
        print("------ BEM VINDO AO INFINITY BANK ---------")
        print("1 - Adicionar conta")
        print("2 - Alterar nome")
        print("3 - Consultar conta")
        print("4 - Remover conta")
        print("5 - Listar contas")
        print("6 - Realizar saque")
        print("7 - Realizar deposito")
        print("8 - Consultar Saldo")
        print("9 - Realizar Transferencia")
        print("10 - Sair")
        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('Digite o saldo do cliente'))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o numero da conta:'))
            nome = input('Digite o novo nome: ')
        elif opcao == 3:
            conta = int(input('Digite o numero da conta: '))
            print(obterConta(conta))
        elif opcao == 4:
            conta = int(input('Digite o numero da conta: '))
            deletarConta(conta)
        elif opcao == 5:
            listarContas()
        elif opcao == 6:
            conta = int(input('Digite o numero da conta: '))
            valor = float(input('Digite o valor que deseja depositar'))
            depositar (conta, valor)
        elif opcao == 7:
            conta = int(input('Digite o numero da conta: '))
            valor = float(input('Digite o valor que deseja sacar'))
            sacar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o numero da conta: '))
            consultarSaldo(conta)
        elif opcao == 9:
            contaOrigem = int(input('informe a conta de origem: '))
            contaDestino = int(input('informe a conta de destino: '))
            valor = float(input('Infome o valor'))
            transferir(contaOrigem, contaDestino, valor)
        elif opcao == 10:
            print('Você saiu do sistema! ')
            break
        else:
            print("Opção invalida")


menu()