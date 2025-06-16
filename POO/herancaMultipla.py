class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # RETORNA O OBJETO EM FORMATO DE STRING 

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)    

class Ave(Animal):
    def __init__(self, cor_bico , **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs) # KW serve para passar argumentos para a classe pai 
        
class Gato(Mamifero):
   pass

class Ornintorrinco(Mamifero, Ave):
    def __init__(self, cor_bico , cor_pelo,nmr_patas):
        print(Ornintorrinco.__mro__)
        super().__init__(nmr_patas = nmr_patas, cor_pelo = cor_pelo, cor_bico= cor_bico) # KW serve para passar argumentos para a classe pai

gato = Gato( nmr_patas= 4, cor_pelo='Preto')# colocar nome dos atributos e valores 
print(gato)  # Output: Animal com 4 patas

ornintorrinco = Ornintorrinco( nmr_patas = 4, cor_pelo='Branco',cor_bico= 'Azul')
print(ornintorrinco)  # Output: Animal com 4 patas, cor