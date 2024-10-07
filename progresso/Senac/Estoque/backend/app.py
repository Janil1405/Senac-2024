from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('estoque.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página principal (visualização do estoque)
@app.route('/')
def index():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

# Rota para lançamento de produtos (entrada e saída)
@app.route('/lancar_estoque', methods=('GET', 'POST'))
def lancar_estoque():
    if request.method == 'POST':
        codigo_barras = request.form['codigo_barras']
        quantidade = int(request.form['quantidade'])
        tipo = request.form['tipo']

        conn = get_db_connection()
        produto = conn.execute('SELECT * FROM produtos WHERE codigo_barras = ?', (codigo_barras,)).fetchone()

        if produto:
            produto_id = produto['id']
            quantidade_atual = produto['quantidade']

            # Atualizar estoque com base na entrada ou saída
            if tipo == 'entrada':
                nova_quantidade = quantidade_atual + quantidade
                conn.execute('UPDATE produtos SET quantidade = ?, data_ultima_compra = ? WHERE id = ?',
                             (nova_quantidade, datetime.now().strftime('%Y-%m-%d'), produto_id))
            elif tipo == 'saida':
                nova_quantidade = quantidade_atual - quantidade if quantidade_atual >= quantidade else quantidade_atual
                conn.execute('UPDATE produtos SET quantidade = ?, data_ultima_saida = ? WHERE id = ?',
                             (nova_quantidade, datetime.now().strftime('%Y-%m-%d'), produto_id))

            # Registrar a movimentação
            conn.execute('INSERT INTO movimentacao (produto_id, tipo, quantidade, data) VALUES (?, ?, ?, ?)',
                         (produto_id, tipo, quantidade, datetime.now().strftime('%Y-%m-%d')))
            conn.commit()
            conn.close()

            return redirect(url_for('index'))
        else:
            conn.close()
            return "Produto não encontrado", 404

    return render_template('lancar_estoque.html')

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
