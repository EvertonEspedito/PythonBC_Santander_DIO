from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
class Veiculo:
  def __init__(self, marca ,modelo,ano ): 
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
  def verificar_antiguidade(self):
    ano_atual = datetime.now().year
    veiculo_ano = ano_atual - self.ano
    if veiculo_ano > 20:
      return "Veiculo Antigo"
    else:
      return "Veiculo Novo"

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())