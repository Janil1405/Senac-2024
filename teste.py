import requests
import csv

# URL da API para os resultados mais recentes da Mega-Sena
url = 'hhttp://localhost:3000/v1/api/megasena/2565'

# Fazendo a requisição para obter os resultados
try:
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    response.raise_for_status()  # Lança um erro se o status não for 200
    dados = response.json()  # Converte a resposta em JSON

    # Extraindo os números sorteados
    numeros_sorteados = dados['dezenas']

    # Exibindo os números sorteados
    print("Números sorteados:", numeros_sorteados)

    # Salvando os resultados em um arquivo CSV
    with open('resultados_megasena.csv', mode='w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Dezenas sorteadas'])
        escritor.writerow(numeros_sorteados)

    print("Os resultados foram armazenados no arquivo 'resultados_megasena.csv'.")

except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API: {e}")
