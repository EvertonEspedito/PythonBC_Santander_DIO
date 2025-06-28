# geradores são funções que retornam valores, mas não armazenam valores em memoria

def gerador():
    for i in range(10):
        yield i
        # o yield é o que torna a função um gerador, ele pausa a execução
        # e retorna o valor, mas não termina a função, ela continua a execução
        # quando chamada novamente
        print(f'Gerador: {i}')

# o gerador é chamado e ele retorna o valor 0
# e pausa a execução, quando chamado novamente ele continua a execução
# e retorna o valor 1, e assim por diante
for valor in gerador():
    print(f'Valor: {valor}')
    # o gerador é chamado e ele retorna o valor 0
    # e pausa a execução, quando chamado novamente ele continua a execução
    # e retorna o valor 1, e assim por diante

