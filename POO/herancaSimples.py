class Veiculo:
    def __init__(self, cor, placa, num_rodas,modelo):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
        self.modelo = modelo

    def ligar_motor(self):
        return f"O veículo {self.modelo} está ligado."
      
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas,modelo, carregado):
        super().__init__(cor, placa, num_rodas,modelo)#poder invocar metodos da classe pai
        self.carregado = carregado

    def estaCarregado(self):# pode colocar coisas especificas
        print(f"{'sim' if self.carregado else 'não'} estou carregado")


moto = Motocicleta('azul', 'ABC123', 2, 'Honda')
print(moto.ligar_motor())  # Output: O veículo Honda está ligado.

carro = Carro('vermelho', 'DEF456', 4, 'Fiat')
print(carro.ligar_motor())  # Output: O veículo Fiat está ligado.

caminhao = Caminhao( 'preto', 'GHI789', 6, 'Mercedes' ,False)
print(caminhao.ligar_motor())  # Output: O veículo Mercedes está ligado
print(caminhao.estaCarregado())  # Output: O caminhão está car