file = open( "arquivo.txt", "r" ) # Abre o arquivo em modo leitura
conteudo = file.read() # lê o conteúdo do arquivo
file.close() # fecha o arquivo
print(conteudo) # imprime o conteúdo do arquivo

file = open( "arquivo.txt", "r" ) # Abre o arquivo em modo leitura
print( file.readline()) #  lê a primeira linha do arquivo
print( file.readline()) #   lê a segunda linha do arquivo
print( file.readline()) #  lê a terceira linha do arquivo
file.close() # fecha o arquivo

