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
    print("5 - Encerrar atendimento")
    return input("Digite o número da operação desejada: ")  # Retorna a opção escolhida pelo usuário

def main():
    conta = None  # Inicializa a variável conta como None (nenhuma conta criada)
    while True:
        opcao = menu()  # Exibe o menu e recebe a opção escolhida
        if opcao == "1":
            conta = criar_conta()  # Chama a função para criar uma conta
        elif opcao == "2" and conta:
            verificar_saldo(conta)  # Verifica o saldo se a conta existir
        elif opcao == "3" and conta:
            depositar_dinheiro(conta)  # Deposita dinheiro se a conta existir
        elif opcao == "4" and conta:
            sacar_dinheiro(conta)  # Saca dinheiro se a conta existir
        elif opcao == "5":
            print("Encerrando o atendimento.")  # Encerra o atendimento e sai do loop
            break
        else:
            # Mensagem de erro para opções inválidas ou quando a conta ainda não foi criada
            print("Opção inválida ou conta não criada.")

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
