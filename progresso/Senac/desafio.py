# # Solicita o salário do cliente
# salario = float(input("Informe o seu salário: "))
# # Solicita o valor do empréstimo
# emprestimo = float(input("Informe o valor do empréstimo: "))

# # Calcula os limites de aprovação
# limite_50 = 0.50 * salario
# limite_75 = 0.75 * salario

# # Verifica as condições para aprovação do empréstimo
# if emprestimo <= limite_50:
#     print("Empréstimo aprovado!")
# elif emprestimo <= limite_75:
#     print("Situação em análise.")
# else:
#     print("Empréstimo não aprovado.")


# um cliente  ira solicitar um emprestimo ao banco. se o valor do esmprestimo for menor ou igual a 50% do seu salario, então o emprestimo sera aprovado.senao, se o Valor 
# do esmprestimo for menor igula a 75% do salario a situação ficara emn analise. senao, informe ao cliente que o esmprestimo nao foi aprovado.


# salário do cliente
salario = int(input("Informe o seu salário: "))
# valor do empréstimo
emprestimo = int(input("Informe o valor do empréstimo: "))

# condições para aprovação do empréstimo
if emprestimo <= salario * 0.50:
    print("Empréstimo aprovado!")
elif emprestimo <= salario * 0.75:
    print("Situação em análise.")
else:
    print("Empréstimo não aprovado.")
