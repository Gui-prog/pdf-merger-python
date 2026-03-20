import PyPDF2
import os

def merger_pdfs(pastas, saida):
    merger = PyPDF2.PdfMerger()

    if not os.path.exists(pastas):
        print(f'Pasta {pastas} não encontrada!')
        return
    
    arquivos = os.listdir(pastas)

    arquivos.sort()

    for lista_arquivos in arquivos:
        if lista_arquivos.lower().endswith(".pdf"):
            caminho = os.path.join(pastas, lista_arquivos)
            merger.append(caminho)

    merger.write(saida)
    merger.close()

merger_pdfs("arquivos", "PDF.FINAL2.pdf")



