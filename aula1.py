# resultado = 10/0
# print(resultado)


# try:
#     resultado = 10/0

# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")
    
# try:
#     resultado = 10/2
    
# except ZeroDivisionError:
#     print("Erro: Divisão por zerto não permitida.")

# else:
#     print(f"O resultado é {resultado}")
    
# try:
#     arquivo = open('dados.txt', 'r')
#     conteudo = arquivo.read()
#     print(conteudo)
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")
# finally:
#     print("Operação Finalizada!")

# try:
#     num = int(input("Digite um número: "))
#     resultado = 100/num
# except ValueError:
#     print("Erro: Você deve digitar um número inteiro.")
# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida.")
# else:
#     print(f"O resultado é {resultado}")
# finally:
#     print("Obrigado por usar o programa")

# def verifica_idade(idade):
#     if idade < 18:
#         raise ValueError 
    

# class SaldoInsuficienteError(Exception):
#     """ Exceção levantada quando o saldo é insuficiente para realizar uma transação"""
#     pass
# def sacar(valor, saldo):
#     if valor > saldo:
#         raise SaldoInsuficienteError ("Saldo insuficiente para sacar o valor solicitado")
#     saldo -= valor
#     return saldo
# try:
#     saldo_atual = sacar(900,1000)
# except SaldoInsuficienteError as e:
#     print(e)
# else:
#     print(saldo_atual)

def get_element_by_index():
    try:
        # Solicita ao usuário uma lista de números
        user_input = input("Digite uma lista de números, separados por espaço: ")
        num_list = list(map(float, user_input.split()))

        # Solicita o índice
        index = int(input("Digite o índice do elemento que deseja acessar: "))

        # Retorna o elemento no índice especificado
        print(f"O elemento no índice {index} é: {num_list[index]}")

    except ValueError:
        print("Erro: Certifique-se de inserir números válidos e um índice inteiro.")
    except IndexError:
        print("Erro: O índice está fora do intervalo da lista.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Exemplo de uso
get_element_by_index()
