import sqlite3

# Conectando ao banco de dados (ou criando se não existir)
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criando tabela de Produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_barras TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    quantidade INTEGER DEFAULT 0,
    data_ultima_compra TEXT,
    data_ultima_saida TEXT
)
''')

# Criando tabela de Movimentação de Estoque
cursor.execute('''
CREATE TABLE IF NOT EXISTS movimentacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER,
    tipo TEXT NOT NULL, -- entrada ou saída
    quantidade INTEGER NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES produtos (id)
)
''')

conn.commit()
conn.close()
