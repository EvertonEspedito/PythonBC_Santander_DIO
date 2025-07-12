import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/ "meu_banco.db")
cursor = conexao.cursor()

def buscar_id( cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?',(id,))#Retorna toda a linha
    cursor.execute('SELECT nome FROM clientes WHERE id = ?',(id,))#Retorna apenas nome
    resultado = cursor.fetchone()
    return resultado

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes')#Todos os dados de todas as linhas



clientes = listar_clientes(cursor)
for linha in clientes:
    print(linha)


cliente = buscar_id(cursor,6)
print(cliente[1])  