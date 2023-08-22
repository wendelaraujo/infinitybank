from banco import obterConta, banco

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print("Deposito realizado com sucesso!")
    else:
        print('Conta não existe!')


if __name__ == "__main__":
    depositar(1, 215.65)
    print(banco)