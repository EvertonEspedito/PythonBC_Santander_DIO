class Bicicleta:
    def __init__(self, valor, modelo, cor, ano):
        self.cor = cor
        self.valor =valor
        self.modelo = modelo
        self.ano = ano

    def buzinar(self):
        print("Bim Bim Bim")

    def parar(self):
        print("Parando...")
        print("Parado!")

    def correr(self):
        print("Correndo...")

b1 = Bicicleta(1500, "caloi 45", "Verde", 2040)    

b1.buzinar()
b1.correr()
b1.parar()
print(b1.modelo) # Parei no 9:15