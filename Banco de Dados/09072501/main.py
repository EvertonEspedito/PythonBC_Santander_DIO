# Criando um banco de dados
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/ "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor,):
    # criar tabelas
    cursor.execute('CREATE TABLE clientes (id INTEGER  PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
    conexao.commit()

def inserir_registro(conexao, cursor,nome,email):
    # inserir registros
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome,email) VALUES(?,?)', data)
    conexao.commit()

def atualizar_registros(conexao, cursor,nome,email, id):   
    #Atualização de Registros
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome = ?,email = ? WHERE id = ?',data) #Atualizar item/ WHERE é importante para atualizar apenas a linha desejada
    conexao.commit()

def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id = ?',data)
    conexao.commit()
    
#adição de varios de dados
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome,email) VALUES(?,?)',dados)
    conexao.commit()


dados = [
    ('Everton Lindão','Everton@lindojhnonson@gmail'),
    ('Erick Cartman', 'gordinho@gmail.com'),
    ('Jackson do JD', 'jdowiodwo@gmail.com')
]
inserir_muitos(conexao,cursor,dados)    