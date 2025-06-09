valorConta = 0.0

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
        print("\nErro ao sacar, valor invalido ou acima!\n")
        return valorConta
    else:
        valorConta -= valerSaque
        print("\n - Valor sacado com sucesso!\n")      
        return valorConta


while True:
    # Solicitar o valor da conta
    print("Selecione a opção para realizar a transação:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Sair")
    opcao = input("Opção: \n")
    
    if opcao == "1":
        valor = float(input("Digite o valor para depositar: R$ "))
        valorConta = depositar(valor,valorConta)
        
    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: R$ "))
        valorConta = sacar(valor,valorConta)

    elif opcao == "3":
        print(f"\n - Seu saldo atual é: R$ {valorConta:.2f}\n")

    elif opcao == "4":
        print("\n - Obrigado por utilizar o sistema!\n")
        break





