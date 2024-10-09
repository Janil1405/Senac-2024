# import mysql.connector
# import datetime

# # Conectar ao banco de dados MySQL
# conn = mysql.connector.connect(
#     host="172.16.100.1",  # ou IP do servidor remoto
#     user="dsouza",
#     password="u55wgan3",
#     database="controle_patrimonio"
# )
# c = conn.cursor()

# # Criar tabela se não existir
# c.execute('''
# CREATE TABLE IF NOT EXISTS colaboradores (
#     matricula VARCHAR(10) PRIMARY KEY,
#     nome VARCHAR(100)
# )
# ''')

# c.execute('''
# CREATE TABLE IF NOT EXISTS registros (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     matricula VARCHAR(10),
#     patrimonio VARCHAR(50),
#     entrada DATETIME,
#     saida DATETIME,
#     observacao_estado TEXT,
#     FOREIGN KEY (matricula) REFERENCES colaboradores (matricula)
# )
# ''')
# conn.commit()

# def cadastrar_colaborador(matricula, nome):
#     try:
#         c.execute('''
#         INSERT INTO colaboradores (matricula, nome)
#         VALUES (%s, %s)
#         ''', (matricula, nome))
#         conn.commit()
#         print(f"Colaborador {nome} cadastrado com matrícula {matricula}.")
#     except mysql.connector.IntegrityError:
#         print("Erro: Matrícula já cadastrada.")

# def registrar_entrada(matricula, patrimonio, observacao_estado):
#     if not matricula or not patrimonio:
#         print("Erro: Todos os campos devem ser preenchidos.")
#         return
    
#     horario_entrada = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     try:
#         c.execute('''
#         INSERT INTO registros (matricula, patrimonio, entrada, observacao_estado)
#         VALUES (%s, %s, %s, %s)
#         ''', (matricula, patrimonio, horario_entrada, observacao_estado))
#         conn.commit()
#         print(f"Entrada registrada: matrícula {matricula} pegou o patrimônio {patrimonio} em {horario_entrada}.")
#     except Exception as e:
#         print(f"Erro ao registrar entrada: {e}")

# def registrar_saida(matricula):
#     horario_saida = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     try:
#         c.execute('''
#         UPDATE registros
#         SET saida = %s
#         WHERE matricula = %s AND saida IS NULL
#         ''', (horario_saida, matricula))
#         conn.commit()
#         if c.rowcount == 1:
#             print(f"Saída registrada para matrícula {matricula} em {horario_saida}.")
#         else:
#             print("Erro: Matrícula não encontrada ou saída já registrada.")
#     except Exception as e:
#         print(f"Erro ao registrar saída: {e}")

# def mostrar_dashboard():
#     print("\n--- Dashboard de Patrimônio ---")
#     print(f"{'Matrícula':<15} {'Nome':<20} {'Patrimônio':<15} {'Entrada':<25} {'Saída':<25} {'Observação':<25}")
#     print("-" * 120)
#     try:
#         c.execute('''
#         SELECT r.matricula, c.nome, r.patrimonio, r.entrada, r.saida, r.observacao_estado
#         FROM registros r
#         JOIN colaboradores c ON r.matricula = c.matricula
#         ''')
#         for row in c.fetchall():
#             matricula, nome, patrimonio, entrada, saida, observacao = row
#             saida_display = saida if saida else "Em uso"
#             print(f"{matricula:<15} {nome:<20} {patrimonio:<15} {entrada:<25} {saida_display:<25} {observacao:<25}")
#     except Exception as e:
#         print(f"Erro ao mostrar o dashboard: {e}")

# # Loop principal (mesmo código para interação)


print("Iniciando o sistema de controle de rádios...")

# Conectar ao banco de dados MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",  # ou IP do servidor remoto
        user="seu_usuario",
        password="sua_senha",
        database="controle_radio"
    )
    c = conn.cursor()
    print("Conexão com o banco de dados estabelecida.")
except mysql.connector.Error as err:
    print(f"Erro de conexão: {err}")
    exit()

# Verifique o loop principal
while True:
    print("Loop principal iniciado.")
    # Código existente do sistema
    # Exemplo de menu:
    print("\nSistema de Controle de Rádio")
    print("1. Cadastrar colaborador")
    print("2. Registrar entrada")
    print("3. Registrar saída")
    print("4. Mostrar dashboard")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '5':
        break
