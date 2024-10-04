import PyPDF2

# Caminho para o arquivo PDF
caminho_pdf = 'seu_arquivo.pdf'

# Lendo o arquivo PDF
try:
    with open(caminho_pdf, 'rb') as arquivo:
        leitor_pdf = PyPDF2.PdfReader(arquivo)

        # Extraindo texto de cada página
        for pagina in leitor_pdf.pages:
            texto = pagina.extract_text()
            if texto:  # Verificando se há texto na página
                print(texto)

except FileNotFoundError:
    print(f"Arquivo não encontrado: {caminho_pdf}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

