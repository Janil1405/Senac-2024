# # Sintaxe básica

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
        
# pessoa1 = Pessoa("Maria", 30)
# print(pessoa1.nome)
# print(pessoa1.idade)

# pessoa2 = Pessoa("Chico", 40)
# print(pessoa2.nome)
# print(pessoa2.idade)
        

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
        
#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
    
# pessoa1 = Pessoa("Maria", 30)
# print(pessoa1.nome)
# print(pessoa1.idade)
# pessoa1.apresentar()


from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def calcular_ano_nascimento(self):
        ano_atual = datetime.now().year
        ano_nascimento = ano_atual - self.idade
        return ano_nascimento

# Usando a classe
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

pessoa = Pessoa(nome, idade)
ano_nascimento = pessoa.calcular_ano_nascimento()

print(f"{pessoa.nome}, você nasceu em {ano_nascimento}.")

