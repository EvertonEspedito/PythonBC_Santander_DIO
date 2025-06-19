# @Abstractmethod todas a class com classe abstrata, precisa ter todos os métodos declarados como abstractmethod
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleDeTV( ControleRemoto):
    
    def ligar(self):
        print( "TV ligada" )
    
    def desligar(self):
        print( "TV desligada" )

controle = ControleDeTV()
# @Abstractmethod eu preciso criar os metodos ligar e desligar dentro da classe ControleDeTV
controle.ligar()
controle.desligar()