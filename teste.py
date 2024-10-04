print("São Francisco de Assis")

lista = [1,2,3,4,5,6,7,8,9]
for i in lista:
    print(i**9)


import csv

# Lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9,11,34]

# Abrindo um arquivo CSV para escrita
with open('resultados.csv', mode='w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    
    # Iterando pela lista e escrevendo os resultados no CSV
    for i in lista:
        resultado = i ** 9
        escritor.writerow([i, resultado])  # Escreve o número e seu resultado

print("Os resultados foram armazenados no arquivo 'resultados.csv'.")
