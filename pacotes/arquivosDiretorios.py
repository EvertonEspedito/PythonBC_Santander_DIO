import os
from pathlib import Path

ROOT_PATH = Path(__file__).parent  # pasta raiz do projeto

# Cria um novo diretório
os.mkdir(ROOT_PATH / 'novo_diretorio')

# Cria e escreve no arquivo
arquivo = open(ROOT_PATH /'novo_diretorio'/ 'arquivo.txt', 'w')
arquivo.write('Olá, mundo!')
arquivo.close()

# Renomeia o arquivo
os.rename(ROOT_PATH /'novo_diretorio'/ 'arquivo.txt',ROOT_PATH /'novo_diretorio'/ 'novo_arquivo.txt')

# remover arquivo
#os.remove(ROOT_PATH /'novo_diretorio'/ 'novo_arquivo.txt')
#remover diretorio
#os.rmdir(ROOT_PATH /'novo_diretorio')
