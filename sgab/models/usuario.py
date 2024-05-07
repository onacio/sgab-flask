from sgab.db.conexao import Conexao


class Usuario:
    def __init__(self, nome, sobrenome, usuario, senha, email, funcao, unidade, status):
        self.nome = nome
        self.sobrenome = sobrenome
        self.usuario = usuario
        self.senha = senha
        self.email = email
        self.funcao = funcao
        self.unidade = unidade
        self.status = status

        self.criar_tabela()

    @staticmethod
    def listar_todos():
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute('SELECT * FROM usuarios')
            dados = cur.fetchall()    
            con.close()

            return dados
        except:
            print("Erro ao listar usuários")

    @staticmethod
    def excluir(id_usuario):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            con.commit()
            con.close()
        except:
            print('erro ao excluir dado')

    @staticmethod
    def editar(id_usuario):        
        try:
            con = Conexao().conectar()
            cur = con.cursor()
            cur.execute("UPDATE FROM usuarios WHERE id = ?", (id_usuario,))
            con.commit()
            con.close()
        except:
            print('erro ao editar dado', )

    def inserir(self):
        sql = '''
            INSERT INTO usuarios (nome, sobrenome, usuario, senha, email, funcao, setor, status) 
            VALUES (?,?,?,?,?,?,?,?);
        '''
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql, (self.nome, self.sobrenome, self.usuario, self.senha, self.email, self.funcao, self.unidade, self.status))
        con.commit()
        con.close()
        
    def criar_tabela(self):
        sql_tabela_usuarios = '''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT (100) NOT NULL,
                sobrenome TEXT (200),
                usuario TEXT (100) NOT NULL UNIQUE,
                senha TEXT (100) NOT NULL,
                email TEXT (200) UNIQUE NOT NULL,
                funcao TEXT NOT NULL,
                setor TEXT (100)  NOT NULL,
                status INTEGER (1) NOT NULL
            );
        '''   
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql_tabela_usuarios)
        con.close()