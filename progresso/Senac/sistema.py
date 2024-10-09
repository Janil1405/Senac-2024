def obter_detalhes_pedido():
    
    pedido = {
        "item": "Notebook",
        "preço": 1200.00,
        "quantidade": 2
    }
    print("Detalhes do pedido obtidos.")
    return pedido

def calcular_preco_total(pedido):
    preco_total = pedido['preco'] * pedido['quantidade']
    print(f"Preço total calculado: R${preco_total}")
    return preco_total
