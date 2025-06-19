class Estudante:
    escola = 'DIO'
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f'{self.nome} - {self.numero} - {self.escola}'
    
def mostrar_alunor(*obj):# função que recebe qualquer tipo de objeto e varios objetos
 for ob in obj:
    print(ob)

gui = Estudante( "Guilherme", 31234)
gi = Estudante( "Giovana", 23123)    
mostrar_alunor(gui, gi) #mostra os dados dos dois alunos

gui.numero = 1

mostrar_alunor(gui, gi) #mostra os dados dos dois alunos
