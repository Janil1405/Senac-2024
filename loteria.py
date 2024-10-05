import pdfplumber
import pandas as pd

# Caminho para o arquivo PDF
pdf_path = r'C:/Users/janil/OneDrive/Documentos/GitHub/Senac-2024/resultados.pdf'

# Função para extrair dados do PDF
def extrair_dados_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        todas_tabelas = []
        
        # Iterar sobre todas as páginas do PDF
        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:
                # Adicionar todas as tabelas extraídas à lista
                todas_tabelas.extend(tabela)
                
    # Remover linhas vazias ou linhas com dados incorretos (se necessário)
    dados_limpios = [linha for linha in todas_tabelas if any(linha)]
    
    # Converter a tabela em um DataFrame do pandas
    df = pd.DataFrame(dados_limpios[1:], columns=dados_limpios[0])
    
    # Exibir os primeiros registros para verificar
    print("\nVisualizando as primeiras linhas da tabela extraída:")
    print(df.head())
    
    return df

# Extrair os dados e exibir a tabela
df_resultados = extrair_dados_pdf(pdf_path)

# Salvando o DataFrame em um arquivo Excel
df_resultados.to_excel(r'C:/Users/janil/OneDrive/Documentos/GitHub/Senac-2024/resultados_megasena.xlsx', index=False)

print("Arquivo Excel salvo com sucesso!")
