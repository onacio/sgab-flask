from sgab.db.conexao import Conexao


class Unidade:
    def __init__(self, nome, cnes, ine):
        self.nome = nome
        self.cnes = cnes
        self.ine = ine

        #self.criar_tabela()

    @staticmethod
    def listar_todos():
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute('SELECT * FROM unidades')
            dados = cur.fetchall()    
            con.close()

            return dados
        except:
            print("Erro ao listar todos as unidades")

    def inserir(self):
        sql = '''
            INSERT INTO unidades (nome, cnes, ine) VALUES (?,?,?);
        '''
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql, (self.nome, self.cnes, self.ine))
        con.commit()
        con.close()

    @staticmethod
    def excluir(id_unidade):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("DELETE FROM unidades WHERE id = ?", (id_unidade,))
            con.commit()
            con.close()
        except:
            print('erro ao excluir dado')
        
    def criar_tabela(self):
        sql_tabela_unidades = '''
            CREATE TABLE IF NOT EXISTS unidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT (100) NOT NULL UNIQUE,
                cnes INTEGER (7) NOT NULL UNIQUE,
                ine INTEGER (15) NOT NULL UNIQUE
            );
        '''   
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql_tabela_unidades)
        con.close()