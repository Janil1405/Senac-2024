# 1. Faça um programa para imprimir:



def print_pattern(n):
    for i in range(1, n+1):
        print((str(i) + ' ') * i)

# Exemplo de uso
n = 5  # Número de linhas a serem impressas
print_pattern(n)
