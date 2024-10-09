import requests
import random
from collections import Counter

# URL da API pública para obter os resultados da Mega-Sena
API_URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"

# Função para consultar a API e obter os últimos resultados
def obter_resultados_mega():
    response = requests.get(API_URL)
    if response.status_code == 200:
        dados = response.json()
        resultados = dados["listaDezenas"]
        return resultados
    else:
        print("Erro ao consultar a API.")
        return []

# Função para gerar os 6 números com base em probabilidades
def gerar_numeros_com_probabilidade():
    todos_numeros = []
    
    # Vamos buscar os resultados de vários concursos (últimos 10 para o exemplo)
    for i in range(10):  # Aqui você pode ajustar a quantidade de concursos que deseja consultar
        numeros_concurso = obter_resultados_mega()
        if numeros_concurso:
            todos_numeros.extend(numeros_concurso)
    
    # Contagem da frequência de cada número
    frequencias = Counter(todos_numeros)
    
    # Obter os números mais frequentes
    mais_frequentes = frequencias.most_common(60)  # Consideramos os números de 1 a 60
    numeros, probabilidades = zip(*mais_frequentes)
    
    # Normalizar as probabilidades para usar no random.choices
    total_frequencias = sum(probabilidades)
    probabilidades_normalizadas = [p / total_frequencias for p in probabilidades]
    
    # Gerar 6 números com base nas probabilidades
    numeros_sorteados = random.choices(numeros, weights=probabilidades_normalizadas, k=6)
    
    return sorted(numeros_sorteados)

# Função principal
def main():
    print("Gerando números com base em probabilidades dos últimos concursos da Mega-Sena...")
    numeros_gerados = gerar_numeros_com_probabilidade()
    print(f"Números gerados: {numeros_gerados}")

if __name__ == "__main__":
    main()
