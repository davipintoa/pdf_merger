
import os
from pypdf import PdfWriter, PdfReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(filename, text):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

if not os.path.exists('input'):
    os.makedirs('input')

create_pdf('input/1.pdf', "This is document 1")
create_pdf('input/2.pdf', "This is document 2")
create_pdf('input/3.pdf', "This is document 3")

print("Created 3 dummy PDFs in 'input' folder.")
