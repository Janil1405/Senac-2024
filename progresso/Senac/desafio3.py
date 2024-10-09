# Questão 11: Crie um dicionário chamado aluno
aluno = {
    "nome": "Daniel bezerra",
    "idade": 40,
    "nota": 9.2
}

# Questão 12: Adicione uma nova chave "curso" ao dicionário aluno
aluno["curso"] = "Ciência da Computação"

# Questão 13: Acesse e imprima o valor da chave "nome" no dicionário aluno.
print(aluno["nome"])

# Questão 14: Remova a chave "nota" do dcionário aluno.
del aluno ["nota"]

# Questão 15: Verifique se a chave "idade" está presente no dicionário aluno e imprima o resultado.
print("idade" in aluno)
print()
print()



# Strings

# Questão 16: Crie uma string chamada frase com o valor "Estruturas de Dados em Python".
frase = "Estruturas de Dados em Python"

# Questão 17: Converta a string frase para letras maiúsculas
frase_maiuscula = frase.upper()
print(frase_maiuscula)
print()

# Questão 18: Encontre a posição da palavra "Dados"
posicao_dados = frase.find("Dados")
print(posicao_dados)
print()

# Questão 19: Substitua "Python" por "Java"
frase_substituida = frase.replace("Python", "Java")
print(frase_substituida)
print()

# Questão 20: Divida a string frase em uma lista de palavras
lista_palavras = frase.split()
print(lista_palavras)