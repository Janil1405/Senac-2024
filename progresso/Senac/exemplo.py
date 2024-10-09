# def saudacao():
#     print("Olá, Bem-Vindo(a) à aula de funções em Python!")
        
# saudacao()
# print()


# def saudacao(nome="aluno "):
#     print(f"Olá, {nome}Bem-Vindo(a) à aula de funções em Python!")
        
# saudacao()
# saudacao("Daniel ")

# def somar(a, b):
#     return a + b

# resultado = somar (10,20)
# print(resultado)



# def checar_numero(n):
#     if n > 2:
#         return "Positivo"
#     elif n < 5:
#         return "Negativo"
#     else:
#         return "Zero"
    
# print(checar_numero(1))


# Define uma variável global chamada global_var e a inicializa com o valor 100
# global_var = 100

# # Define uma função chamada exemplo_escopo
# def exemplo_escopo():
#     # Dentro da função, define uma variável local chamada local_var e a inicializa com uma string
#     local_var = "Estou dentro da função"
    
#     # Imprime o valor da variável local
#     print(local_var)
    
#     # Imprime o valor da variável global, que foi definida fora da função
#     print(global_var)

# # Chama a função exemplo_escopo, que executa o código dentro dela
# exemplo_escopo()

# # Tenta imprimir o valor da variável local_var. Isso resultará em um erro.
# print(local_var)

# def exibir_nome_idade(nome, idade, numero=1):
#     print(f"Nome: {nome}, é: {idade},{numero}")
    
# exibir_nome_idade(idade=40, nome="nevou")
# exibir_nome_idade(idade=40, nome="nevou",numero=10)


# def somar_todos(*args):
#     return sum(args)

# print(somar_todos(1, 2, 3, 4, 5)) 


def exibir_detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
        
# Coletando entradas do usuário
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
cidade = input("Digite a cidade: ")

      
# Chama a função com os dados inseridos pelo usuário
exibir_detalhes(nome=nome, idade=idade, cidade=cidade)
