import PyPDF2

# Abre o arquivo PDF
with open('resultados.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Obtém o número de páginas
    num_pages = len(pdf_reader.pages)

    # Extrai o texto da primeira página
    page = pdf_reader.pages[0]
    text = page.extract_text()

    print(text)
    
    import tabula

# Extrai todas as tabelas do PDF em DataFrames
dfs = tabula.read_pdf("meu_pdf.pdf", pages='all')

# Acessando a primeira tabela
df = dfs[0]

print(df)