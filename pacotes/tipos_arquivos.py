#Arquivos CSV 
#Aqui você pode criar um arquivo CSV com as informações que você deseja
import csv
with open('arquivo.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nome', 'Idade'])  # Nome da coluna 'Nome'
    writer.writerow(['João', 25])  # Nome e idade de João

#Arquivos JSON
#Aqui você pode criar um arquivo JSON com as informações que você deseja
import json
with open('arquivo.json', 'w') as jsonfile:
    dados = {'nome': 'João', 'idade': 25}
    json.dump(dados, jsonfile)
