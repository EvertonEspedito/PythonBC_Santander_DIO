#Não existe encapsulamento em Python, mas podemos usar classes para criar objetos que encapsulem dados e métodos. Existe apenas como uma conversão!
class Conta:
    def __init__(self, nro_agencia ,saldo = 0 ): 
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def MostrarSaldo(self):
        return self._saldo

conta = Conta(1234 ,1000)
print(conta._saldo)  #esta errado! o _ é apenas uma convenção para indicar que é um atributo privado, mas não é uma proteção real

conta.sacar(500)  # por isso é interessante usar METODOS!
conta.depositar(3000)
print(conta.MostrarSaldo()) # Essa é a forma correta de acessar o atributo! pois o método MostrarSaldo() acessa o atributo _saldo e o retorna!
print (conta.nro_agencia)  # esse pode ser acessado diretamente, pois não está encapsulado
