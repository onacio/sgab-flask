from sgab.db.conexao import Conexao


class Itens():
    def __init__(self, descricao, categoria, status=0):
        self.descricao = descricao
        self.categoria = categoria
        self.status = status

    def listar_todos():
        try:
            conexao = Conexao().conectar()
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM itens_pedidos")
            itens = cursor.fetchall()
            conexao.close()
            return itens
        except Exception as erro:
            raise erro

    def inserir(self):
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("INSERT INTO itens_pedidos (descricao, categoria, status) VALUES (?,?,?);", (self.descricao, self.categoria, self.status))
            con.commit()
            con.close()
        except Exception as erro:            
            raise erro

    @staticmethod
    def listar_categoria(categoria):
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("SELECT * FROM itens_pedidos WHERE categoria = ?", (categoria,))
            categoria = cur.fetchall()    
            con.close()

            return categoria
        except Exception as erro:            
            raise erro