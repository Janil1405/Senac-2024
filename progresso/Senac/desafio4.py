def obter_detalhes_pedido():
    # Simula a obtenção de detalhes de um pedido
    pedido = {
        "item": "Notebook",
        "preco": 1200.00,
        "quantidade": 2
    }
    print("Detalhes do pedido obtidos.")
    return pedido

def calcular_preco_total(pedido):
    # Calcula o preço total do pedido
    preco_total = pedido['preco'] * pedido['quantidade']
    print(f"Preço total calculado: R${preco_total}")
    return preco_total

def enviar_confirmacao(pedido, preco_total):
    # Simula o envio de uma confirmação de pedido
    print(f"Confirmação enviada para {pedido['quantidade']} {pedido['item']}(s).")
    print(f"Valor total a ser pago: R${preco_total}")

def processar_pedido():
    # Chama as funções auxiliares para processar o pedido
    pedido = obter_detalhes_pedido()
    preco_total = calcular_preco_total(pedido)
    enviar_confirmacao(pedido, preco_total)

# Chamando a função principal
processar_pedido()


