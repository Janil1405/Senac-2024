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


# from datetime import datetime

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def calcular_ano_nascimento(self):
#         ano_atual = datetime.now().year
#         ano_nascimento = ano_atual - self.idade
#         return ano_nascimento

# # Usando a classe
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# pessoa = Pessoa(nome, idade)
# ano_nascimento = pessoa.calcular_ano_nascimento()

# print(f"{pessoa.nome}, você nasceu em {ano_nascimento}.")

# from datetime import datetime

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def calcular_ano_nascimento(self):
#         ano_atual = datetime.now().year
#         ano_nascimento = ano_atual - self.idade
#         return ano_nascimento

# def main():
#     resultados = []

#     while True:
#         nome = input("Digite seu nome (ou 'sair' para finalizar): ")
#         if nome.lower() == 'sair':
#             break
#         idade = int(input("Digite sua idade: "))

#         pessoa = Pessoa(nome, idade)
#         ano_nascimento = pessoa.calcular_ano_nascimento()
        
#         resultado = f"{pessoa.nome}, você nasceu em {ano_nascimento}."
#         print(resultado)
#         resultados.append(resultado)

#     # Armazenando os resultados em um arquivo
#     with open('resultados.txt', 'w') as arquivo:
#         for resultado in resultados:
#             arquivo.write(resultado + '\n')

#     print("Os resultados foram armazenados no arquivo 'resultados.txt'.")

# if __name__ == "__main__":
#     main()


# class Carro:
#     def __init__(self, motor, rodas, farois):
#         self.motor = motor
#         self.rodas = rodas
#         self.farois = farois

#     def ligar(self):
#         print("Carro ligado")

#     def desligar(self):
#         print("Carro desligado")
        
# # Criando um objeto da classe Carro
# meu_carro = Carro(motor="gasolina", rodas=4, farois="acesos")

# # Usando os métodos
# meu_carro.ligar()    # Saída: Carro ligado
# meu_carro.desligar() # Saída: Carro desligado


# class Carro:
#     total_de_carros = 6

#     def __init__(self, cor):
#         self.cor = cor
#         Carro.total_de_carros += 1
    
#     @classmethod
#     def mostrar_total(cls):
#         print(f"Total de carros: {cls.total_de_carros}")

# carro1 = Carro("azul")
# carro2 = Carro("vermelho")
# Carro.mostrar_total()  # Saída: Total de carros: 2

# class Carro:
#     @staticmethod
#     def tipo_de_combustivel():
#         return "Gasolina, Etanol, Elétrico"

# print(Carro.tipo_de_combustivel())  # Saída: Gasolina, Etanol, Elétrico



<<<<<<< HEAD
# class Pessoa:
#     def __init__(self,nome):
#         self.__nome = nome
#     @property #getters
#     def nome(self):
#         return self.__nome
#     @nome.setter #setters
#     def nome(self, novo_nome):
#         if isinstance(novo_nome, str) and novo_nome.strip():
#             self.__nome = novo_nome
#         else:
#             print("Nome inválido")

# #Uso da classe

# pessoa = Pessoa("Alice")
# print(pessoa.nome)
# pessoa.nome = "Bob"
# print(pessoa.nome)
# pessoa.nome=""


x = 1
n = 5
for i in range(n):
    print(i-1)

=======

def bubble_sort(a_list):
    list_length = len(a_list) -1
    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list

a_list = [10, 1, 12, 9, 2]
print(bubble_sort(a_list))

print(len(a_list))
      
>>>>>>> 37842ddb116dce190338fe33565c093bc47d323b
