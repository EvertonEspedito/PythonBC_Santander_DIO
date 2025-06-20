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
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
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

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self._limite_saque

        if excedeu_limite:
            print('Erro: Valor excede o limite permitido para saque.')
        elif excedeu_saques:
            print('Erro: Limite de quantidade de saques excedido.')
        elif valor > 0:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            print(f'Saque realizado com sucesso. Saldo atual: {self._saldo}')
            return True
        else:
            print('Valor inválido para saque.')

        return False

    def __str__(self):
        return f"""
Conta Corrente {self.numero} - {self.cliente.nome}
Saldo: {self.saldo}
Limite de saque: {self.limite}
Limite de saques diários: {self._limite_saque}
"""


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
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
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
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
