from fpdf import FPDF

class Relatorio:
    def __init__(self, dados): 
        self.dados = dados
        self.pdf = FPDF(orientation='P', unit='mm', format='A4')        
        self.cabecalho()
        self.titulo()
        self.conteudo()
        self.pdf.output('relatorio.pdf')

    def cabecalho(self):        
        self.pdf.add_page()
        self.pdf.set_font('Arial', '', 12)
        self.pdf.image(x=12, y=7, name='sgab/static/img/logo_maragogipe.png', w=20, h=20)
        self.pdf.text(x=35, y=13, txt='PREFEITURA MUNICPAL DE MARAGOGIPE')
        self.pdf.text(x=35, y=18, txt='SECRETARIA MUNICPAL DE SAÚDE')
        self.pdf.text(x=35, y=23, txt='COORDENAÇÃO DE ATENÇÃO BÁSICA')

    def titulo(self):                
        self.pdf.set_font('Arial', 'B', 13)        
        # self.pdf.text(x=70, y=40, txt='Relatório de Unidades de Saúde')
        self.pdf.set_y(40)
        self.pdf.cell(w=210, h=8, txt='Relatório de Unidades de Saúde', align='C')
        self.pdf.set_font('Arial', '', 12)        
        self.pdf.text(x=10, y=60, txt='Nome')                        
        self.pdf.text(x=146, y=60, txt='CNES')        
        self.pdf.text(x=175, y=60, txt='INE')    
        self.pdf.dashed_line(x1=10, x2=200, y1=63, y2=63)    

    def conteudo(self):        
        
        self.pdf.set_x(10)
        self.pdf.set_y(65)
        
        for linha in self.dados:
            
            self.pdf.set_font('Arial', '', 12)                   
            self.pdf.cell(w=135, h=8, txt=linha[1])
            self.pdf.cell(w=29, h=8, txt=str(linha[3]))            
            self.pdf.cell(w=30, h=8, txt=str(linha[4]), ln=True)