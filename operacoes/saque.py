from banco import obterConta, banco

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print('Saque realizado com sucesso')
        else:
            print('Saldo insuficiente')
    else:
        print('Conta não existe!')

if __name__ == "__main__":
    sacar(1, 500)
    print(banco)
    sacar(1, 500)
    print(banco)
    sacar(1, 500)
    print(banco)
    sacar(1, 500)
    print(banco)
    sacar(3, 100)
    print(banco)