# Sintaxe básica

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
pessoa1 = Pessoa("Maria", 30)
print(pessoa1.nome)
print(pessoa1.idade)

pessoa2 = Pessoa("Chico", 40)
print(pessoa2.nome)
print(pessoa2.idade)
        