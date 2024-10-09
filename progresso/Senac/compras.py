import json

# Função para carregar compras de um arquivo
def carregar_compras():
    try:
        with open('compras.txt', 'r') as file:
            return json.load(file)  # Carrega a lista de compras do arquivo
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir

# Função para salvar compras em um arquivo
def salvar_compras(compras):
    with open('compras.txt', 'w') as file:
        json.dump(compras, file)  # Salva a lista de compras no arquivo

# Inicializando a lista de compras
compras = carregar_compras()  # Carrega as compras ao iniciar o programa

# Loop principal do programa
while True:
    # Exibindo o menu
    print("\nMenu:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Exibir lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        codigo = input("Digite o código do produto: ")
        item = input("Digite o item que deseja adicionar: ")
        
        # Lista de entradas a serem solicitadas
        entradas = [('valor', 'Digite o valor: '), ('quantidade', 'Digite a quantidade: ')]
        valores = {}
        
        # Loop para coletar valores
        for chave, mensagem in entradas:
            while True:
                valor = input(mensagem)
                try:
                    if chave == 'valor':
                        valor_float = float(valor)
                        if valor_float < 0:
                            print("Por favor, insira um valor positivo.")
                        else:
                            valores[chave] = valor_float1
                            break
                    elif chave == 'quantidade':
                        quantidade_int = int(valor)
                        if quantidade_int <= 0:
                            print("Por favor, insira uma quantidade positiva.")
                        else:
                            valores[chave] = quantidade_int
                            break
                except ValueError:
                    print(f"{mensagem} inválido. Por favor, insira um número.")

        # Adicionando o item à lista de compras como um dicionário
        compras.append({'codigo': codigo, 'item': item, 'valor': valores['valor'], 'quantidade': valores['quantidade']})
        print(f"Item '{item}' adicionado à lista.")
        salvar_compras(compras)  # Salva a lista após adicionar o item

    elif opcao == '2':
        codigo = input("Digite o código do produto que deseja remover: ")
        # Encontrando o item na lista de compras
        for compra in compras:
            if compra['codigo'] == codigo:
                compras.remove(compra)
                print(f"Item '{compra['item']}' removido da lista.")
                salvar_compras(compras)  # Salva a lista após remover o item
                break
        else:
            print(f"Produto com código '{codigo}' não encontrado na lista.")

    elif opcao == '3':
        # Exibindo a lista de compras
        print("\nLista de Compras:")
        print(f"{'Código':<10} {'Item':<20} {'Valor':<10} {'Quantidade':<10} {'Total':<10}")
        print("-" * 70)
        total_geral = 0
        for compra in compras:
            item_total = compra['valor'] * compra['quantidade']
            total_geral += item_total
            print(f"{compra['codigo']:<10} {compra['item']:<20} {compra['valor']:<10.2f} {compra['quantidade']:<10} {item_total:<10.2f}")
        print("-" * 70)
        print(f"{'Total a ser gasto:':<40} {total_geral:<10.2f}")

    elif opcao == '4':
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
