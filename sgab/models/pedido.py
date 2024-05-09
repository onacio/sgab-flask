from datetime import datetime
from sgab.db.conexao import Conexao

class Pedido:
    def __init__(self, categoria, item, unidade_saude, quantidade='', quantidade_liberada='', justificativa='', data_finalizacao='', status='0'):
        self.data_pedido = datetime.now()
        self.categoria = categoria
        self.item = item
        self.quantidade = quantidade
        self.quantidade_liberada = quantidade_liberada
        self.unidade_saude = unidade_saude
        self.justificativa = justificativa
        self.data_finalizacao = data_finalizacao
        self.status = status

        self.criar_tabela()

    def inserir(self):
        sql = '''
            INSERT INTO pedidos (
                data_pedido, categoria, item, quantidade, quantidade_liberada, unidade_saude, justificativa, data_finalizacao, status
            ) VALUES (?,?,?,?,?,?,?,?,?);
        '''
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql, (self.data_pedido, self.categoria, self.item, self.quantidade, self.quantidade_liberada, self.unidade_saude, self.justificativa, self.data_finalizacao, self.status))
        con.commit()
        con.close()

    
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