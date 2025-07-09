# Criando um banco de dados
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/ "meu_banco.db")
cursor = conexao.cursor()
# criar tabelas
cursor.execute('CREATE TABLE clientes (id INTEGER  PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
# inserir registros

data = ('Everton', 'everton@gmail.com')
cursor.execute('INSERT INTO clientes (nome,email) VALUES(?,?)', data)
conexao.commit()

