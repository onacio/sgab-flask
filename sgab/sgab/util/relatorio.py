from fpdf import FPDF


class Relatorio:
    def __init__(self, dados, autor): 
        self.dados = dados
        self.autor = autor
        self.pdf = FPDF(orientation='P', unit='mm', format='A4')        
        self.cabecalho()
        self.titulo()
        self.conteudo()
        self.footer()
        self.pdf.output('sgab/static/files/relatorio.pdf')        

    def cabecalho(self):        
        self.pdf.add_page()
        self.pdf.set_font('Arial', '', 12)
        self.pdf.image(x=12, y=7, name='sgab/static/img/logo_maragogipe.png', w=20, h=20)
        self.pdf.text(x=35, y=13, txt='PREFEITURA MUNICPAL DE MARAGOGIPE')
        self.pdf.text(x=35, y=18, txt='SECRETARIA MUNICPAL DE SAÚDE')
        self.pdf.text(x=35, y=23, txt='COORDENAÇÃO DE ATENÇÃO BÁSICA')

    def titulo(self):                
        self.pdf.set_font('Arial', 'B', 13)                
        self.pdf.set_y(40)        
        self.pdf.cell(w=190, h=8, txt='Unidades de Saúde da Família', align='C')
        self.pdf.set_font('Arial', '', 12)        
        self.pdf.text(x=10, y=60, txt='Nome')                        
        self.pdf.text(x=146, y=60, txt='CNES')        
        self.pdf.text(x=175, y=60, txt='INE')    
        self.pdf.line(x1=10, x2=200, y1=63, y2=63)    

    def conteudo(self):        
        self.pdf.set_x(10)
        self.pdf.set_y(65)        
        for linha in self.dados:            
            self.pdf.set_font('Arial', '', 12)                   
            self.pdf.cell(w=135, h=8, txt=linha[1])
            self.pdf.cell(w=29, h=8, txt=str(linha[3]))            
            self.pdf.cell(w=30, h=8, txt=str(linha[4]), ln=True)                
    
    def footer(self):
        # Select Arial italic 8
        self.pdf.set_font('Arial', 'I', 8)
        # Imprime o nome  do autor no rodapé
        self.pdf.text(x=5, y=292, txt=f'Impresso por: {self.autor}')
        # Imprime a página atual no rodapé
        self.pdf.text(x=191, y=292, txt=f'Página {self.pdf.page_no()}')