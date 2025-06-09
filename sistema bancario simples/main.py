valorConta = 0.0
saqueCount = 0

def depositar(valerDepo, valorConta):
    if ( valerDepo <= 0 ):
        print("\n - Erro ao depositar, valor invalido!\n")
        return valorConta
    else:
        valorConta += valerDepo
        print("\n - Valor depositado com sucesso!\n")
        return valorConta

def sacar(valerSaque, valorConta):
    if ( valerSaque > valorConta  or valerSaque < 0):
        if ( valerSaque >= 500.0):
            print("\n - Erro ao sacar, valor acima dos 500.00!\n")
        print("\nErro ao sacar, valor invalido!\n")
        return valorConta
    else:
        valorConta -= valerSaque
        print("\n - Valor sacado com sucesso!\n")      
        return valorConta
    
def lineMenu():
    for i in range(1, 52):
        print("=", end="")


while True:
    # Menu
    lineMenu()
    print("\n - Banco Digital - Menu\n")
    print("Selecione a opção para realizar a transação:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Sair")
    lineMenu()
    opcao = input("\nOpção: \n")
    lineMenu()
    if opcao == "1":
        valor = float(input("\nDigite o valor para depositar: R$ \n"))
        valorConta = depositar(valor,valorConta)
        
    elif opcao == "2":
        print(f"\nApenas 3 saques diarios, você já fez {saqueCount} saque(s)\n")
        if saqueCount <=3:
            valor = float(input("\nDigite o valor para sacar: R$ \n"))
            valorConta = sacar(valor,valorConta)
            saqueCount += 1

        if saqueCount == 3:
            lineMenu()
            print("\n - Você atingiu o limite de 3 saques diários!\n")

    elif opcao == "3":
        lineMenu()
        print(f"\n - Seu saldo atual é: R$ {valorConta:.2f}\n")
        lineMenu()

    elif opcao == "4":
        lineMenu()
        print("\n - Obrigado por utilizar o sistema!\n")
        lineMenu()
        break
    lineMenu()


