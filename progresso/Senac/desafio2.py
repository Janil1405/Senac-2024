# minhaLista = [76, 92.3, "oi", True, 4, 76]
# print(minhaLista)

# # a) Inserir "pera" e 76 no final da lista
# minhaLista.insert("")


# # Criando a lista
# minhaLista = [76, 92.3, "oi", True, 4, 76]

# # a) Inserir “pera” e 76 no final da lista.
# minhaLista.append("pera")
# minhaLista.append(76)

# # b) Inserir o valor “gato” na posição de índice 3.
# minhaLista.insert(3, "gato")

# # c) Inserir o valor 99 no início da lista.
# minhaLista.insert(0, 99)

# # d) Encontrar o índice de “oi”.
# indice_oi = minhaLista.index("oi")

# # e) Remover True da lista.
# minhaLista.remove(True)

# # Exibindo a lista e o índice encontrado
# print("Lista:", minhaLista)
# print("Índice de 'oi':", indice_oi)

# uma_lista = [4,2,8,6,5]
# # uma_lista = uma_lista + ['gato,' 'bode', 'bola']

# tupla = (1, 2, 3, "quatro")
# print(tupla[0])
# print(tupla[3])

# # Criando a lista
# minhaLista = [76, 92.3, "oi", True, 4, 76]

# # Adicionando itens usando append
# minhaLista.append("pera")  # Adiciona "pera"
# minhaLista.append(76)      # Adiciona 76

# # Exibindo a lista
# print(minhaLista)

# Listas

# Questão 1: Crie uma lista chamada frutas com os seguintes elementos: "maçã", "banana", "laranja".
frutas = ["maçã", "banana", "laranja"]

# Questão 2: Adicione a fruta "uva" à lista frutas.
frutas.append("uva")

# Questão 3: Remova a fruta "banana" da lista frutas.
frutas.remove("banana")

# Questão 4: Acesse e imprima o segundo elemento da lista frutas.
print("Segundo elemento da lista frutas:", frutas[1])  # Isso imprimirá "laranja"

# Questão 5: Inverta a ordem dos elementos na lista frutas. 
frutas.reverse()
print("Lista frutas após inversão:", frutas)

# Tuplas

# Questão 6: Crie uma tupla chamada cores com os seguintes elementos: "vermelho", "verde", "azul".
cores = ("vermelho", "verde", "azul")

# Questão 7: Acesse e imprima o primeiro e o último elemento da tupla cores.
print("Primeiro elemento da tupla cores:", cores[0])
print("Último elemento da tupla cores:", cores[-1])

# Questão 8: Tente alterar o segundo elemento da tupla cores para "amarelo" e observe o que acontece.
try:
    cores[1] = "amarelo"  # Isso causará um erro
except TypeError as e:
    print("Erro ao tentar alterar a tupla:", e)

# Questão 9: Concatene a tupla cores com outra tupla contendo "amarelo" e "roxo".
novas_cores = cores + ("amarelo", "roxo")
print("Tupla após concatenação:", novas_cores)

# Questão 10: Desempacote a tupla cores em três variáveis cor1, cor2 e cor3.
cor1, cor2, cor3 = cores
print("Cores desempacotadas:", cor1, cor2, cor3)