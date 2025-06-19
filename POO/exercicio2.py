class Pedido:
    def __init__(self):
        self.itens = []  
    
    # Método para adicionar item
    def adicionar_item(self, preco):
        self.itens.append(preco)

    # Método para calcular o total
    def calcular_total(self):
        return sum(self.itens)


quantidade_pedidos = int(input().strip())
pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)  # separa nome e preço
    preco = float(preco)
    pedido.adicionar_item(preco)  # adiciona o item

# Calcula o total após todos os itens serem adicionados
total = pedido.calcular_total()
print(f"{total:.2f}")
