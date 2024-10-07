# # frutas = ["maçã", "banana", "laranja"]

# # for fruta in frutas:
# #     print(fruta)
    

# # for i in range(92):
# #     print(i)

# # soma = 0 

# # # Soma os números de 1 a 10
# # for i in range(1, 11):
# #     soma += i  # Corrigido: a sintaxe de soma deve ser 'soma += i'
# #     a  = 0
# #     b = 10
# #     print(soma)  
# #     print(a) # escopo local e escopo global
# # # Imprime o resultado da soma

# # print("A soma de 1 a 10 é:", soma)
# # print(a)

# # palavra = "Python"

# # for letra in palavra:
# #     print(letra)
    
#     # Usando o exemplo anterior, como fariamos para imprimir a letra e seu respectivo indice? "a letra P tem indice 0"
    
# #     texto = "Python"

# # for i in range(len(texto)):
# #     print(f"A letra '{texto[i]}' tem índice {i}.")
    
# # palavra = "Teste"

# # for i in range(len(palavra)):
# #     print(f"A letra '{palavra[i]}' tem índice {i}.")

# # exemplo

# # frase = input(" Digite uma frase: ").lower()
# # vogais = "aeiou"
# # contador = 0
# # contador2 = 0

# # for letra in frase:
# #     if letra in vogais:
# #         contador += 1
# #     else:
# #         contador2 +=1
        
# # print(f" Há {contador} vogais na frase. {contador2} Consoantes")

# # 1. escreva um programa que imprima os numeros de 1 a 10 usando um laço for.
# # for i in range(1, 11):
# #     print(i)
# # print()

# # # 2. Escreva um programa que some todos os números de 1 a 50 e imprima o resultado.

# # soma = 0
# # for i in range(1, 51):
# #     soma += i

# # print("O Resultado é:", soma)
# # print()

# # 3. escreva um programa que solicite um numero e exiba a tabuada. exe: (5x1, 5x2, ..., 5x10).

# numero = int(input("Digite o valor : "))

# print(f"Tabuada do {numero}:")
# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")
# print()

# # 4. Use um laçõ for para imprimir todos os numeros parees de 0 a 20.

# for i in range(0, 21, 2):
#     print(i)

# # 5. Dada a string frase = "Python é divertido!", use um for para contar quantas letras existem na frase (descosidere espaços).

# frase = "Python é divertido!"
# contador = sum(1 for letra in frase if letra.isalpha())

# print("Número de letras na frase:", contador)
# print()

# # 6. Dada uma lista numeros = [1,2,3,4,5], use um laço for para criar uma nova lista com os elementos na ordem inversa.

# numeros = [1, 2, 3, 4, 5]
# numeros_invertidos = []

# for numero in numeros[::-1]:  
#     numeros_invertidos.append(numero)

# print("Lista invertida:", numeros_invertidos)
# print()

# # 7. Escreva um programa que receba um numero inteiro n do usuario e imprima todos os numeros primos mmenores que n.

# Solicita um número inteiro ao usuário
n = int(input("Digite um número inteiro: "))

# Loop para encontrar e imprimir números primos menores que n
for num in range(2, n):
    primo = True  # Assume que o número é primo

    # Verifica se o número é divisível por qualquer número até sua raiz quadrada
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False  # Não é primo
            break

    # Se for primo, imprime o número
    if primo:
        print(num)
