import os
from reportlab.pdfgen import canvas

# --- Criação das pastas ---
pastas = ["pdfs", "xmls", "txts"]
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)

# --- Criar PDF ---
pdf_path = os.path.join("pdfs", "arquivo.pdf")
c = canvas.Canvas(pdf_path)
c.showPage()
c.save()

# --- Criar XML ---
xml_path = os.path.join("xmls", "arquivo.xml")
open(xml_path, "w", encoding="utf-8").close()

# --- Criar TXT ---
txt_path = os.path.join("txts", "arquivo.txt")
open(txt_path, "w", encoding="utf-8").close()

print("Arquivos vazios criados com sucesso!")
