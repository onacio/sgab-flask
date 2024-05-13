from datetime import datetime
from sgab.db.conexao import Conexao


class Pedido:
    def __init__(self, descricao_item, categoria, unidade_saude, quantidade='', quantidade_liberada='', justificativa='', data_finalizacao='', status=0):
        self.data_pedido = datetime.now().strftime("%d/%m/%Y-%H:%M")
        self.descricao_item = descricao_item
        self.categoria = categoria
        self.quantidade = quantidade
        self.quantidade_liberada = quantidade_liberada
        self.unidade_saude = unidade_saude
        self.justificativa = justificativa
        self.data_finalizacao = data_finalizacao
        self.status = status

        self.criar_tabela()

    @staticmethod
    def listar_todos():
        try:            
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute('SELECT * FROM pedidos')
            pedidos = cur.fetchall()
            con.close()

            return pedidos        
        except:
            print('')
    
    @staticmethod
    def listar_um(id_pedido):
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("SELECT * FROM pedidos WHERE id = ?", (id_pedido,))
            pedido = cur.fetchone()
            return pedido
        except:
            print('')

    def inserir(self):
        sql = '''
            INSERT INTO pedidos (
                data_pedido, descricao_item, categoria, quantidade, quantidade_liberada, unidade_saude, justificativa, data_finalizacao, status
            ) VALUES (?,?,?,?,?,?,?,?,?);
        '''
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql, (self.data_pedido, self.descricao_item, self.categoria, self.quantidade, self.quantidade_liberada, self.unidade_saude, self.justificativa, self.data_finalizacao, self.status))
        con.commit()
        con.close()

    @staticmethod
    def excluir(id_pedido):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("DELETE FROM pedidos WHERE id = ?", (id_pedido,))
            con.commit()
            con.close()            
        except:
            print('Erro ao excluir pedido')

    @staticmethod
    def alterar(id_pedido, qtde):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("UPDATE pedidos SET quantidade_liberada = ?, status = ? WHERE id = ?;", (qtde, 1, id_pedido))
            con.commit()
            con.close()            
        except:
            print('Erro ao atender o pedido')
    
    def criar_tabela(self):
        sql_tabela_pedidos = '''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                data_pedido TEXT (100) NOT NULL,
                categoria TEXT (100) NOT NULL,
                item TEXT (100) NOT NULL,
                quantidade INTEGER NOT NULL,
                quantidade_liberada INTEGER NOT NULL,
                unidade_saude TEXT (100) NOT NULL,
                justificativa TEXT NOT NULL,
                data_finalizacao TEXT (100) NOT NULL,
                status INTEGER (1) NOT NULL,
                usuario_id INTEGER NOT NULL,
                unidade_id INTEGER NOT NULL
            );
        '''   
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql_tabela_pedidos)
        con.close()