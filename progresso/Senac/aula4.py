# # Declarando dicionários
# dic = {}
# print(type(dic))  # Mostra que 'dic' é um dicionário vazio
# print(1)  # Linha em branco

# # Criando um dicionário com times e suas contagens de títulos
# dic_pernambuco = {"Sport": 41, "Santa Cruz": 29, "Nautico": 21, "Teste": 1}
# print(dic_pernambuco)  # Exibe o dicionário inicial
# print(2)  # Linha em branco

# # Adicionando um elemento no dicionário
# dic_pernambuco["Salgueiro"] = 1  # Adiciona "Salgueiro" com valor 1
# print(dic_pernambuco)  # Exibe o dicionário após a adição
# print(3)  # Linha em branco

# # Alterando o valor de 'Sport' para uma lista de anos
# dic_pernambuco["Sport"] = [1987, 1990, 2008]  # Muda o valor da chave "Sport"
# print(dic_pernambuco)  # Exibe o dicionário com a alteração
# print(4)  # Linha em branco

# # Buscando valor com base na chave
# qnt_titulos = dic_pernambuco.get("Sport")  # Obtém o valor da chave "Sport"
# print(qnt_titulos)  # Exibe a lista de anos
# print("O Sport tem", len(qnt_titulos), "títulos")  # Mostra o número de títulos
# print(5)  # Linha em branco

# # Remover um elemento com base na chave
# del dic_pernambuco["Salgueiro"]  # Remove a chave "Salgueiro" sem retornar o valor
# print(dic_pernambuco)  # Exibe o dicionário após remoção de "Salgueiro"
# print(6)  # Linha em branco

# # Remove a chave e retorna seu valor
# valor = dic_pernambuco.pop("Nautico")  # Remove "Nautico" e guarda seu valor na variável 'valor'
# print("O valor retornado da chave é:", valor)  # Exibe o valor removido
# print(dic_pernambuco)  # Exibe o dicionário após remoção de "Nautico"
# print(7)  # Linha em branco

# # Verificar se uma chave existe no dicionário
# print("Teste" in dic_pernambuco)  # Retorna True se "Teste" estiver no dicionário
# print(8)  # Linha em branco

# # Pegar todas as chaves do dicionário
# print(dic_pernambuco.keys())  # Exibe todas as chaves do dicionário
# print(9)  # Linha em branco

# # Pegar todos os valores do dicionário
# teste = dic_pernambuco.values()  # Obtém todos os valores do dicionário
# print(teste)  # Exibe todos os valores
# print(10)  # Linha em branco

# # Converter chaves e valores para listas
# chaves_lista = list(dic_pernambuco.keys())  # Converte as chaves em uma lista
# valores_lista = list(dic_pernambuco.values())  # Converte os valores em uma lista

# print("Chaves como lista:", chaves_lista)  # Exibe as chaves como lista
# print("Valores como lista:", valores_lista)  # Exibe os valores como lista
# print(11)  # Linha em branco

# # Se você quiser acessar um valor específico, pode fazer assim:
# # Por exemplo, acessar o valor associado à chave "Sport"
# if "Teste" in dic_pernambuco:  # Verifica se a chave "Sport" existe
#     print("Os anos em que o Sport ganhou títulos são:", dic_pernambuco["Sport"])  # Exibe os anos
# print(12)  # Linha em branco

# # Criando um segundo dicionário com times de São Paulo
# dic_paulista = {"Corinthians": 30, "Santos": 22, "Palmeiras": 22}

# # Removendo e retornando o último elemento
# print(dic_paulista.popitem())  # Remove e retorna o último item do dicionário
# print(dic_paulista)  # Exibe o dicionário após a remoção do último item
# print(13)  # Linha em branco

# # Mesclar dois dicionários
# dic_pernambuco.update(dic_paulista)  # Adiciona os itens de dic_paulista a dic_pernambuco
# print(dic_pernambuco)  # Exibe o dicionário mesclado
# print(14)  # Linha em branco

# # Convertendo um dicionário em uma lista
# print(list(dic_pernambuco))  # Exibe as chaves do dicionário como uma lista
# print(list(dic_pernambuco.values()))  # Exibe os valores do dicionário como uma lista
# print(15)  # Linha em branco
# print()

# # Atenção: Usem o print para retornar o valor das variaveis !!!
# # Declarando uma string

# mensagem = " Hello, World"

# # Concatenando strings:
# primeiro_nome = "João"
# sobrenome = "Silva"
# nome_completo = primeiro_nome + " " + sobrenome
# print(nome_completo)
# print()

# # Acessando caracteres individuais em uma string:

# mensagem = "Hello, World"
# primeiro_caractere = mensagem[0]
# ultimo_caractere = mensagem[-1]
# print(primeiro_caractere)
# print(ultimo_caractere)
# print()

# # Encontrando o comprimento de uma string

# mensagem = "Hello, World"
# comprimento = len(mensagem)
# print(comprimento)
# print()

# # Conevertendo uma string para letras maiuscula ou minuscula

# mensagem = "Hello, World!"
# maiuscula = mensagem.upper()
# minuscula = mensagem.lower()
# print(maiuscula)
# print(minuscula)
# print()

# # Dividindo uma string em substring com base em um delimitador
# mensagem = "Hello, World!"
# palavras = mensagem.split(",")
# print(palavras)
# print()

# # Verificando se uma substring está presente em uma string:

# mensagem = "Hello, World!"
# if "world" in mensagem:
#     print("a substring 'world' está presente na mensagem")
# print()
    
# # Substituindo caracteres em uma string:

# mensagem = "Hello, World!"
# nova_mensagem = mensagem.replace("Hello", "Python","Daniel",)
# print(nova_mensagem)
# print()

frase = "    Hello, World!    "
letras_pares = frase[::2]
print(letras_pares)

frase = "     Hello, World!!      "
sem_espacos = frase.strip()
print(sem_espacos)