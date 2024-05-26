from datetime import datetime
from sgab.db.conexao import Conexao


class Pedido:
    def __init__(self, descricao, categoria, solicitante, quantidade, quantidade_liberada, justificativa='', data_finalizacao='', status=0):
        self.data_pedido = datetime.now().strftime("%d/%m/%Y")
        self.hora_pedido = datetime.now().strftime("%H:%M")
        self.descricao = descricao
        self.categoria = categoria
        self.quantidade = quantidade
        self.quantidade_liberada = quantidade_liberada
        self.solicitante = solicitante
        self.justificativa = justificativa
        self.data_finalizacao = data_finalizacao
        self.status = status
        
    @staticmethod
    def listar_todos():
        try:            
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute('SELECT * FROM pedidos')
            pedidos = cur.fetchall()
            con.close()            
            return pedidos        
        except Exception as erro:
            raise erro
    
    @staticmethod
    def listar_um(id_pedido):
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("SELECT * FROM pedidos WHERE id = ?", (id_pedido,))
            pedido = cur.fetchone()
            return pedido
        except Exception as erro:
            raise erro

    def inserir(self):
        try:
            sql = '''
                INSERT INTO pedidos (
                    data_pedido, hora_pedido, descricao_item, categoria, quantidade, quantidade_liberada, solicitante, justificativa, data_finalizacao, status
                ) VALUES (?,?,?,?,?,?,?,?,?,?);
            '''
            conexao = Conexao().conectar()
            cursor = conexao.cursor()
            cursor.execute(sql, (self.data_pedido, 
                                 self.hora_pedido, 
                                 self.descricao, 
                                 self.categoria, 
                                 self.quantidade, 
                                 self.quantidade_liberada, 
                                 self.solicitante, 
                                 self.justificativa, 
                                 self.data_finalizacao, 
                                 self.status))
            conexao.commit()
            conexao.close()
        except Exception as erro:
            raise erro

    @staticmethod
    def excluir(id_pedido):        
        try:
            conexao = Conexao().conectar()
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM pedidos WHERE id = ?", (id_pedido,))
            conexao.commit()
            conexao.close()            
        except Exception as erro:
            raise erro

    @staticmethod
    def alterar(id_pedido, qtde, status, data):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("UPDATE pedidos SET quantidade_liberada = ?, status = ?, data_finalizacao = ? WHERE id = ?;", (qtde, status, data, id_pedido))
            con.commit()
            con.close()            
        except Exception as erro:
            raise erro
    
    def criar_tabela(self):
        sql_tabela_pedidos = '''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                data_pedido TEXT NOT NULL,
                hora_pedido TEXT NOT NULL,
                categoria TEXT (100) NOT NULL,
                descricao_item TEXT (100) NOT NULL,
                quantidade INTEGER NOT NULL,
                quantidade_liberada INTEGER NOT NULL,
                solicitante TEXT (100) NOT NULL,
                justificativa TEXT NOT NULL,
                data_finalizacao TEXT (100) NOT NULL,
                status INTEGER (1) NOT NULL                
            );
        '''   
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql_tabela_pedidos)
        con.close()