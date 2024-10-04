    
try:
    arquivo = open('dados.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
finally:
    print("Operação Finalizada!")