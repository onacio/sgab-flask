from services.conexao_banco import Conexao

class Pedido:
    def __init__(self, pedido, valor):        
        self.pedido = pedido
        self.valor = valor

    # def criar_tabela(self):
    #     conexao = Conexao()
    #     conexao.conectar()
        
    #     sql = '''CREATE TABLE pedido (
    #                     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                     pedido TEXT NOT NULL,
    #                     valor REAL NOT NULL
    #                 );'''
        
    #     conexao.executar_comando(sql)
        
    #     conexao.desconectar()
        

    def inserir(self):
        conexao = Conexao().conectar()        
        cursor = conexao.cursor()
        
        cursor.execute("INSERT INTO pedido (pedido, valor) VALUES (?,?)", (self.pedido, self.valor,))
        conexao.commit()
        
        conexao.close()
        
