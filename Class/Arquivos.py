import os
import random
import shutil
from reportlab.pdfgen import canvas
from Utils.gerarNomeArquivo import gerarNomeArquivo

class Arquivos:
    def __init__(self): 
        print("Classe Arquivos Iniciando")
        self.pastas = ["pdfs", "xmls", "txts"]

    def criarArquivoPDF(self, pasta):
        pdf_path = os.path.join(f"arquivos/{pasta}", f"{gerarNomeArquivo()}.pdf")
        c = canvas.Canvas(pdf_path)
        c.showPage()
        c.save()

    def criarArquivoXML(self, pasta): 
        xml_path = os.path.join(f"arquivos/{pasta}", f"{gerarNomeArquivo()}.xml")
        open(xml_path, "w", encoding="utf-8").close()

    def criarArquivoTXT(self, pasta): 
        txt_path = os.path.join(f"arquivos/{pasta}", f"{gerarNomeArquivo()}.txt")
        open(txt_path, "w", encoding="utf-8").close()

    def criarPastas(self): 
        for pasta in self.pastas:
            os.makedirs(f"arquivos/{pasta}", exist_ok=True)
        print(f"Pastas criadas: {self.pastas}")

    def criarArquivos(self, qtd = 3):
        self.criarPastas()
        for _ in range(qtd):
            pasta_aleatoria = random.choice(self.pastas)
            i = random.randint(1, 3)

            if (i == 1):
                self.criarArquivoPDF(pasta_aleatoria)
            elif (i == 2):
                self.criarArquivoXML(pasta_aleatoria)
            elif (i == 3): 
                self.criarArquivoTXT(pasta_aleatoria)
    

    def organizarArquivos(self):
        base_dir = "arquivos"
        self.criarPastas()

        for pasta in self.pastas:
            caminho_pasta = os.path.join(base_dir, pasta)

            for arquivo in os.listdir(caminho_pasta):
                caminho_arquivo = os.path.join(caminho_pasta, arquivo)

                if os.path.isdir(caminho_arquivo):
                    continue

                if arquivo.endswith(".pdf"):
                    destino = os.path.join(base_dir, "pdfs", arquivo)
                elif arquivo.endswith(".xml"):
                    destino = os.path.join(base_dir, "xmls", arquivo)
                elif arquivo.endswith(".txt"):
                    destino = os.path.join(base_dir, "txts", arquivo)
                else:
                    continue 

                if caminho_arquivo != destino:
                    os.makedirs(os.path.dirname(destino), exist_ok=True)
                    os.rename(caminho_arquivo, destino)
                    print(f"Movido: {arquivo} → {destino}")
    
    def deletarTudo(self):
        base_dir = "arquivos"

        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
            print(f"Toda a pasta '{base_dir}' e seu conteúdo foram deletados.")
        else:
            print("A pasta 'arquivos' não existe.")



