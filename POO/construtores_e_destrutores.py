class Cachorro:
    def __init__(self, nome, idade, raca): # inicializa os atributos Construtor é o método que inicializa os atributos de uma classe: __init__
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        return f"{self.nome} está latindo!"
    
    def comer(self):
        return f"{self.nome} está comendo!"
    
    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Raça: {self.raca}"
    
    def __del__(self):
        print(f"O cachorro {self.nome} foi eliminado da memória!") # método destrutor, é chamado quando o objeto é eliminado da memória é executado por ultimo automaticamente, ,as pode invocar antes
    
c1 = Cachorro("Tupan", 7, "Vira-Lata")

print(c1.latir())   
print(c1.comer())
print(c1.info())