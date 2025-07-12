import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def buscar_id(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    return cursor.fetchone()  # Retorna (id, nome, email)

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes')  # Retorna todos os registros

# Listar todos os clientes
clientes = listar_clientes(cursor)
for linha in clientes:
    print(linha)

# Buscar cliente com ID 
cliente = buscar_id(cursor, 6)
if cliente:
    print(cliente[1])  # Nome do cliente
else:
    print("Cliente com ID 6 não encontrado.")

#Buscar ID, via unput
id = input("Digite o Id que deseja")
cliente = buscar_id(cursor, id)
if cliente:
    print('ID VALIDO!')
    print(cliente[1])
else:
    print(f"Cliente com ID {id} não encontrado.")

