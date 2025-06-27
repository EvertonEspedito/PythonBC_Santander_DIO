#Iteradores é uma forma de acessar os elementos de uma coleção sem precisar de índices.
#O iterador é uma classe que implementa o método __iter__ e o método __next
#é usado para acessar os elementos da coleção.
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)
    # O método __iter__ é usado para criar um iterador.
    def __iter__(self):
        return self
    #O método __next__ é usado para acessar os elementos da coleção.
    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration
        
for line in FileIterator('arquivo.txt'):
    print(line)
            