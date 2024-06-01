import sqlite3

class Conexao:
    def __init__(self):
        self.nome_banco = 'sgab/banco.db'
        self.conexao = None
  
    def conectar(self):        
        try:
            conexao = sqlite3.connect(self.nome_banco)            
            return conexao
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None