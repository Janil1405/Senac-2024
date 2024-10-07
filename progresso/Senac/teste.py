def criar_conta():
    # Função para criar uma nova conta bancária
    # Solicita o nome do titular e cria uma conta com saldo inicial de 0
    conta = {
        "nome": input("Digite o nome do titular: "),  # Pede o nome do titular da conta
        "saldo": 0.0  # Define o saldo inicial como 0.0
    }
    # Exibe a confirmação de criação da conta com o nome do titular e o saldo inicial
    print(f"Conta criada para {conta['nome']} com saldo inicial de R${conta['saldo']:.2f}")
    return conta  # Retorna o dicionário contendo as informações da conta

def verificar_saldo(conta):
    # Função para exibir o saldo atual da conta
    print(f"Saldo atual de {conta['nome']}: R${conta['saldo']:.2f}")

def depositar_dinheiro(conta):
    # Função para depositar dinheiro na conta
    valor = float(input("Digite o valor para depósito: R$"))  # Solicita o valor a ser depositado
    conta['saldo'] += valor  # Adiciona o valor ao saldo da conta
    # Exibe a confirmação do depósito e o novo saldo
    print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${conta['saldo']:.2f}")

def sacar_dinheiro(conta):
    # Função para sacar dinheiro da conta
    valor = float(input("Digite o valor para saque: R$"))  # Solicita o valor a ser sacado
    if valor <= conta['saldo']:  # Verifica se o saldo é suficiente para o saque
        conta['saldo'] -= valor  # Subtrai o valor sacado do saldo
        # Exibe a confirmação do saque e o novo saldo
        print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${conta['saldo']:.2f}")
    else:
        # Exibe uma mensagem de erro se o saldo for insuficiente
        print("Saldo insuficiente para realizar o saque.")

def menu():
    # Função para exibir o menu de operações ao usuário
    print("\nEscolha uma operação:")
    print("1 - Criar conta")
    print("2 - Verificar saldo")
    print("3 - Depositar dinheiro")
    print("4 - Sacar dinheiro")

