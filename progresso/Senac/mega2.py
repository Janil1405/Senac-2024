import sqlite3
import requests
import time
from tqdm import tqdm
import speedtest

# Função para conectar ao banco de dados SQLite
def conectar_banco():
    conn = sqlite3.connect('megasena.db')  # Cria ou conecta ao banco de dados SQLite
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sorteios (
            concurso INTEGER PRIMARY KEY,
            data TEXT,
            dezenas TEXT
        )
    ''')
    conn.commit()
    return conn, cursor

# Função para inserir os dados no banco de dados
def inserir_resultado(concurso, data, dezenas, cursor, conn):
    cursor.execute("INSERT OR IGNORE INTO sorteios (concurso, data, dezenas) VALUES (?, ?, ?)", 
                   (concurso, data, ','.join(map(str, dezenas))))
    conn.commit()

# Função para obter o resultado de um concurso específico da API
def obter_resultado_concurso(concurso_numero):
    url = f"https://loteriascaixa-api.herokuapp.com/api/megasena/{concurso_numero}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        dezenas_sorteadas = [int(dezena) for dezena in dados['dezenas']]
        concurso = dados['concurso']
        data = dados['data']
        return {
            "concurso": concurso,
            "data": data,
            "dezenas": dezenas_sorteadas
        }
    else:
        print(f"Erro ao consultar o concurso {concurso_numero}.")
        return None

# Função para salvar o progresso em um arquivo
def salvar_progresso(concurso_numero):
    with open('progresso.txt', 'w') as f:
        f.write(str(concurso_numero))

# Função para carregar o último progresso
def carregar_progresso():
    try:
        with open('progresso.txt', 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return None  # Se o arquivo não existir, significa que é a primeira vez

# Função para coletar e armazenar todos os sorteios no banco de dados com barra de progresso
def coletar_todos_resultados():
    conn, cursor = conectar_banco()

    # Primeiro, obter o último concurso
    url_ultimo_concurso = "https://loteriascaixa-api.herokuapp.com/api/megasena/latest"
    response = requests.get(url_ultimo_concurso)
    if response.status_code != 200:
        print("Erro ao consultar a API para o último concurso.")
        return

    # Obtém o número do último concurso
    dados = response.json()
    ultimo_concurso_numero = dados['concurso']

    # Carregar progresso anterior
    ultimo_concurso_coletado = carregar_progresso()
    if ultimo_concurso_coletado is None:
        # Se não houver progresso salvo, começamos do concurso mais recente
        ultimo_concurso_coletado = ultimo_concurso_numero

    print(f"Iniciando coleta a partir do concurso {ultimo_concurso_coletado}...")

    # Configurar a barra de progresso
    for concurso_numero in tqdm(range(ultimo_concurso_coletado, 0, -1), desc="Coletando sorteios"):
        resultado = obter_resultado_concurso(concurso_numero)
        if resultado:
            inserir_resultado(
                resultado['concurso'], 
                resultado['data'], 
                resultado['dezenas'], 
                cursor, 
                conn
            )
            # Atualizar progresso a cada concurso coletado
            salvar_progresso(concurso_numero)

        # Pausar por 1 segundo entre as consultas para evitar sobrecarga na API
        time.sleep(1)

    conn.close()

# Função para medir a velocidade da internet
def medir_velocidade_internet():
    try:
        print("Testando a velocidade da internet...")
        st = speedtest.Speedtest()
        st.get_best_server()
        velocidade_download = st.download() / 1_000_000  # Converte para Mbps
        velocidade_upload = st.upload() / 1_000_000  # Converte para Mbps
        print(f"Velocidade de download: {velocidade_download:.2f} Mbps")
        print(f"Velocidade de upload: {velocidade_upload:.2f} Mbps")
    except Exception as e:
        print(f"Erro ao medir a velocidade da internet: {e}")

# Função principal
def main():
    # Testar a velocidade da internet
    medir_velocidade_internet()

    print("Coletando todos os resultados da Mega-Sena e armazenando no banco de dados...")
    coletar_todos_resultados()

if __name__ == "__main__":
    main()
