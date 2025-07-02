file = open( "arquivo.txt", "r" ) # Abre o arquivo em modo leitura
conteudo = file.read() # lê o conteúdo do arquivo
file.close() # fecha o arquivo
print(conteudo) # imprime o conteúdo do arquivo