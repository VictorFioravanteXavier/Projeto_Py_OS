import os
import random
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

    def criarArquivos(self, qtd):
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



