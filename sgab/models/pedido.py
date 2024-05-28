from datetime import datetime
from sgab.db.conexao import Conexao


class Pedido:
    def __init__(self, descricao, categoria, solicitante, quantidade, quantidade_liberada, justificativa='', data_finalizacao='', status=0):
        self.data = datetime.now().strftime("%d/%m/%Y")
        self.hora = datetime.now().strftime("%H:%M")
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
            cur.execute('SELECT * FROM tb_pedidos')
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
            cur.execute("SELECT * FROM tb_pedidos WHERE id = ?", (id_pedido,))
            pedido = cur.fetchone()
            return pedido
        except Exception as erro:
            raise erro

    def inserir(self):
        try:
            sql = '''
                INSERT INTO tb_pedidos (
                    data, hora, descricao, categoria, quantidade, quantidade_liberada, solicitante, justificativa, data_finalizacao, status
                ) VALUES (?,?,?,?,?,?,?,?,?,?);
            '''
            conexao = Conexao().conectar()
            cursor = conexao.cursor()
            cursor.execute(sql, (self.data, 
                                 self.hora, 
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
            cursor.execute("DELETE FROM tb_pedidos WHERE id = ?", (id_pedido,))
            conexao.commit()
            conexao.close()            
        except Exception as erro:
            raise erro

    @staticmethod
    def alterar(id_pedido, qtde, status, data):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("UPDATE tb_pedidos SET quantidade_liberada = ?, status = ?, data_finalizacao = ? WHERE id = ?;", (qtde, status, data, id_pedido))
            con.commit()
            con.close()            
        except Exception as erro:
            raise erro