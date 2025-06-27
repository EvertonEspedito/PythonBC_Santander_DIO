# decoradores é uma função que recebe outra função como argumento e devolve outra função
def calcular(operacao):
    def somar(a,b):
        return a + b
    def subtrair(a,b):
        return a - b
    def multiplicar(a,b):
        return a * b
    def dividir(a,b):
        if b == 0:
            return "Erro: Divisão por zero"
        else:
            return a / b
    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    elif operacao == "*":
        return multiplicar
    elif operacao == "/":
        return dividir
    else:
        return "Erro: Operação inválida"
    
resultado = calcular("+") # ou pode ser assim : resultado = calcular("+") (10,15) 
print(resultado(10, 5))  # Output: 15

resultado = calcular("-") (10,5) #  ou pode ser assim : resultado = calcular("-") (10,5)
print(resultado) 
