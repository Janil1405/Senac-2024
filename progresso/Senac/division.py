# # try:
# #     resultado = 10 / 2
# # except ZeroDivisionError:
# #     print("Não pode dividir por zero.")
# # else:
# #     print(f"O resultado é {resultado}")

# # try:
# #     arquivo = open('comprass.txt', 'r')
# #     conteudo = arquivo.read()
# #     print(conteudo)

# # except FileNotFoundError:
# #     print('Erro: Arquivo não econtrado.')

# # finally:
# # #     print('Operação finalizada.')

# # try:
# #     num = int(input("Digite um número: "))
# #     resultado = 100 / num
# # except ValueError:
# #     print("Erro: voce deve digitar um numero inteiro. ")
# # except ZeroDivisionError:
# #     print("Erro: Divisão por zero não é permitida. ")
# # else:
# #     print(f"O resultado é {resultado}")
# # finally:
# #     print("Obrigado por usar o programa.")
    
    
# # def verifica_idade(idade: int):
# #     if idade < 18:
# #         raise ValueError("Idade dever ser maior ou igual a 18.")
# #     else:
# #         print("Entrada Permitida")

# # try:
# #     verifica_idade(18)
# # except ValueError as e:
# #     print(e)


# class SaldoInsuficienteError(Exception):
#     """Exceção levantada quando o saldo é insuficiente para realizar uma transação."""
#     pass

# def sacar(valor, saldo):
#     # Verificando se valor ou saldo são do tipo str
#     if type(valor) == str or type(saldo) == str:
#         raise TypeError("Os valores de saque e saldo devem ser numéricos, não strings.")
    
#     # Verificando se o valor de saque é maior que o saldo
#     if valor > saldo:
#         raise SaldoInsuficienteError("Saldo insuficiente para sacar o valor solicitado.")
    
#     saldo -= valor
#     return saldo

# try:
#     saldo_atual = sacar("teste", 1500)  # Aqui estamos passando uma string para o valor
# except TypeError as e:
#     print(f"Erro de tipo: {e}")  # Mensagem de erro se os tipos estiverem errados
# except SaldoInsuficienteError as e:
#     print(e)  # Mensagem de erro se o saldo for insuficiente


# # except TypeError:
# #     print("digite apenas")


# Escreva uma função que solicite ao usuario uma lista de numeros e um indica. Retorne o elemento no indice especificado, tratando as execeções que pode ocorrer se o indice forminvalido.

# Crie uma exceção personalizada chamada

# Tarefa 1: Função que retorna um elemento da lista com base no índice fornecido
def get_element_from_list():
    try:
        # Solicita ao usuário uma lista de números
        numbers = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
        index = int(input("Digite o índice que deseja acessar: "))
        # Retorna o elemento no índice especificado
        print(f"O elemento no índice {index} é {numbers[index]}")
    except IndexError:
        print("Erro: O índice fornecido está fora do intervalo da lista.")
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de que está inserindo números.")

# Tarefa 2: Exceção personalizada e função de verificação de senha
class SenhaFracaError(Exception):
    pass

def verifica_senha(senha):
    if len(senha) < 8 or not any(c.islower() for c in senha) or not any(c.isupper() for c in senha) or not any(c.isdigit() for c in senha):
        raise SenhaFracaError("A senha é fraca! Ela deve ter pelo menos 8 caracteres, conter letras maiúsculas, minúsculas e números.")
    else:
        print("Senha forte!")

# Tarefa 3: Calculadora simples com tratamento de exceções
def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Erro: Divisão por zero não permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")
        
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")

# Teste as funções no seu ambiente local:
# get_element_from_list()  # Teste a função de lista
# verifica_senha('SenhaForte123')  # Teste a verificação de senha
# calculadora()  # Teste a calculadora
