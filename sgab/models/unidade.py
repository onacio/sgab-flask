from sgab.db.conexao import Conexao


class Unidade:
    def __init__(self, nome, nome_curto, cnes, ine):
        self.nome = nome
        self.nome_curto = nome_curto
        self.cnes = cnes
        self.ine = ine

    @staticmethod
    def listar_todos():
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute('SELECT * FROM tb_unidades')
            dados = cur.fetchall()    
            con.close()

            return dados
        except:
            print("Erro ao listar todos as unidades")

    def inserir(self):
        sql = '''
            INSERT INTO tb_unidades (nome, nome_curto, cnes, ine) VALUES (?,?,?,?);
        '''
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql, (self.nome, self.nome_curto, self.cnes, self.ine))
        con.commit()
        con.close()

    @staticmethod
    def excluir(id_unidade):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("DELETE FROM tb_unidades WHERE id = ?", (id_unidade,))
            con.commit()
            con.close()
        except:
            print('erro ao excluir dado')