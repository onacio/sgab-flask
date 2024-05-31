from fpdf import FPDF

class Relatorio:
    def __init__(self): 
        pass

    def rel(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font('Arial', '', 16)
        pdf.text(x=100, y=10, txt='PREFEITURA MUNICPAL DE MARAGOGIPE')
        pdf.output('relatorio.pdf')