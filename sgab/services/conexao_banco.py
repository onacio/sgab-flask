import sqlite3

class Conexao:
    def __init__(self):
        self.nome_do_banco='banco.db'
        self.conexao = None
        

    def conectar(self):
        try:
            conexao = sqlite3.connect(self.nome_do_banco)
            #cursor = conexao.cursor()
            if self.conexao != None:
                return self.conexao
            self.conexao = conexao
            return self.conexao
                
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
        
    def desconectar(self):
        self.conexao.close()


        