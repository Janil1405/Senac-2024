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
        

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
    
pessoa1 = Pessoa("Maria", 30)
print(pessoa1.nome)
print(pessoa1.idade)
pessoa1.apresentar()

