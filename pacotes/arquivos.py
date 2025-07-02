file = open( "arquivo.txt", "r" ) # Abre o arquivo em modo leitura
conteudo = file.read() # lê o conteúdo do arquivo
file.close() # fecha o arquivo
print(conteudo) # imprime o conteúdo do arquivo

file = open( "arquivo.txt", "r" ) # Abre o arquivo em modo leitura
print( file.readline()) #  lê a primeira linha do arquivo
print( file.readline()) #   lê a segunda linha do arquivo
print( file.readline()) #  lê a terceira linha do arquivo
file.close() # fecha o arquivo

#Ler arquivo com while
file = open( "arquivo.txt", "r" ) 
while len (file.readline()) > 0: # enquanto houver linhas no arquivo
    print(file.readline()) # imprime a linha
file.close() # fecha o arquivo

file = open( "arquivo.txt", "w" ) # Abre o arquivo em modo escrita
file.write("Linha 1\n") # escreve a primeira linha
file.write("Linha 2\n") # escreve a segunda linha
file.write("Linha 3\n") # escreve a terceira linha
file.writelines (["Linha 4\n ", " Linha 5 "]) # escreve as linhas 4 e 5
file.close() # fecha o arquivo