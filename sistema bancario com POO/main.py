import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


# ==================== Cliente ====================

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# ==================== Conta ====================

class Conta:
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero
        self._saldo = 0.0
        self._agencia = '0001'
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print('Saldo insuficiente')
        elif valor > 0:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            print(f'Saque realizado com sucesso. Saldo atual: {self._saldo}')
            return True
        else:
            print('Valor inválido')
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))
            print(f'Depósito realizado com sucesso. Saldo atual: {self._saldo}')
            return True
        else:
            print('Valor inválido')
        return False

    def exibir_extrato(self):
        print(f"\n=== Extrato da Conta {self.numero} ===")
        for transacao in self.historico.transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print(f"Saldo atual: R$ {self._saldo:.2f}")


# ==================== Conta Corrente ====================

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saque=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([
            transacao for transacao in self._historico.transacoes
            if transacao['tipo'] == 'Saque'
        ])
        if valor > self.limite:
            print('Erro: Valor excede o limite permitido para saque.')
        elif numero_saques >= self._limite_saque:
            print('Erro: Limite de saques excedido.')
        elif valor > 0:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            print(f'Saque realizado com sucesso. Saldo atual: {self._saldo}')
            return True
        else:
            print('Valor inválido')
        return False


# ==================== Histórico ====================

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })


# ==================== Transações ====================

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# ==================== Funções Auxiliares ====================

def menu():
    menu = """\n
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova Conta
[lc]\tListar Contas
[nu]\tNovo Usuário
[q]\tSair
=> """
    return input(textwrap.dedent(menu))


def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("O cliente não tem contas")
        return
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    valor = float(input("Digite o valor a ser depositado: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    valor = float(input("Digite o valor a ser sacado: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    conta = recuperar_conta_cliente(cliente)
    if conta:
        conta.exibir_extrato()


def criar_conta(numero, clientes, contas):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado")
        return
    conta = ContaCorrente(cliente, numero)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("Conta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print(conta)


def criar_cliente(clientes):
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")


# ==================== MAIN ====================

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)
        elif opcao == 's':
            sacar(clientes)
        elif opcao == 'e':
            exibir_extrato(clientes)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'q':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
