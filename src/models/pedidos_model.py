from services.conexao_banco import Conexao
from constantes import CRAR_TABELA_PEDIDOS

class Pedido:
    def __init__(self, descricao, unidade, data):
        self.criar_tabela
        self.descricao = descricao
        self.unidade = unidade
        self.data = data

    def criar_tabela(self):
        conexao = Conexao().conectar()        
        cursor = conexao.cursor()
        
        cursor.execute(CRAR_TABELA_PEDIDOS)
        conexao.commit()
        
        conexao.close()

    def inserir(self):
        conexao = Conexao().conectar()        
        cursor = conexao.cursor()
        
        cursor.execute("INSERT INTO pedidos (descricao, unidade, data) VALUES (?,?,?)", (self.descricao, self.unidade, self.data))
        conexao.commit()
        
        conexao.close()
        
