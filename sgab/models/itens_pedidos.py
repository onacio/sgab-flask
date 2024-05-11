from sgab.db.conexao import Conexao

class Itens():
    def __init__(self, descricao, categoria):
        self.descricao = descricao
        self.categoria = categoria

        self.criar_tabela()

    @staticmethod
    def listar_categoria(categoria):
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("SELECT * FROM itens_pedidos WHERE categoria = ?", (categoria,))
            categoria = cur.fetchall()    
            con.close()

            return categoria
        except:
            print('erro ao retornar categoria')

    @staticmethod
    def criar_tabela(self):
        sql_tabela = '''
            CREATE TABLE IF NOT EXISTS itens_pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                descricao TEXT (100) NOT NULL,
                categoria TEXT (100) NOT NULL               
            );
        '''   
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql_tabela)
        con.close()