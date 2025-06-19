# polimorfismo é a capacidade de uma classe ter métodos com o mesmo nome, mas com diferentes implementações
class Passaro:
    def voar(self): pass

class Pardal(Passaro):
    def voar(self): 
        print("O pardal está voando")

class Avestruz(Passaro):
    def voar(self):
        print("O avestruz não voa")

def plano_de_voo(passaro):
    passaro.voar()
    # polimorfismo em ação

plano_de_voo(Pardal())
plano_de_voo(Avestruz())  # não vai dar erro, pois o método vo
