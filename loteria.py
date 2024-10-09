import itertools
import csv

# Solicitar 10 dezenas do usuário
dezenas = []
print("Insira 10 dezenas (números entre 1 e 60):")

while len(dezenas) < 10:
    try:
        numero = int(input(f"Dezena {len(dezenas) + 1}: "))
        
        # Verificar se o número está entre 1 e 60 e se já não foi inserido
        if 1 <= numero <= 60 and numero not in dezenas:
            dezenas.append(numero)
        else:
            print("Número inválido ou repetido. Tente novamente.")
    
    except ValueError:
        print("Por favor, insira um número válido.")

# Gerar todas as combinações de 6 dezenas a partir das 10 fornecidas
combinacoes = list(itertools.combinations(dezenas, 6))

# Encontrar a combinação de 6 menores dezenas
menores_dezenas = sorted(dezenas)[:6]
soma_menores = sum(menores_dezenas)

# Encontrar a combinação de 6 maiores dezenas
maiores_dezenas = sorted(dezenas, reverse=True)[:6]
soma_maiores = sum(maiores_dezenas)

# Exibir os resultados
print(f"\nAs 6 menores dezenas são: {menores_dezenas}, com soma = {soma_menores}")
print(f"As 6 maiores dezenas são: {maiores_dezenas}, com soma = {soma_maiores}")

# Filtrar combinações onde a soma das dezenas está entre 100 e 200
combinacoes_filtradas = [
    combinacao for combinacao in combinacoes
    if 100 < sum(combinacao) < 200
]

# Exibir o total de combinações filtradas
print(f"\nTotal de combinações geradas: {len(combinacoes)}")
print(f"Total de combinações filtradas (soma entre 100 e 200): {len(combinacoes_filtradas)}")

# Salvar as combinações filtradas em um arquivo CSV
with open("combinacoes_filtradas_megasena.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Combinação", "Dezenas", "Soma"])  # Cabeçalho
    for i, combinacao in enumerate(combinacoes_filtradas, 1):
        writer.writerow([f"Combinação {i}", ", ".join(map(str, combinacao)), sum(combinacao)])

print("Combinações filtradas salvas no arquivo 'combinacoes_filtradas_megasena.csv'.")
