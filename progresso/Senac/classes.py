from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = self.calcular_ano_nascimento()

    def calcular_ano_nascimento(self):
        # Calcula o ano de nascimento a partir da idade
        ano_atual = datetime.now().year
        return ano_atual - self.idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
    def dtnascimento(self):
        print(f"Eu nasci no ano de {self.ano_nascimento}.")

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("Maria", 30)
pessoa1.apresentar()
pessoa1.dtnascimento()

pessoa2 = Pessoa("Chico", 31)
pessoa2.apresentar()
pessoa2.dtnascimento()

pessoa3 = Pessoa("Daniel Bezerra", 41)
pessoa3.apresentar()
pessoa3.dtnascimento()