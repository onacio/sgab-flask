from sgab.db.conexao import Conexao

class Usuario:
    def __init__(self, nome, sobrenome, usuario, senha, email, funcao, setor, status):
        self.nome = nome
        self.sobrenome = sobrenome
        self.usuario = usuario
        self.senha = senha
        self.email = email
        self.funcao = funcao
        self.setor = setor
        self.status = status

        self.criar_tabela()

    def listar(self):
        pass

    def inserir(self):
        sql = '''
            INSERT INTO usuarios (nome, sobrenome, usuario, senha, email, funcao, setor, status) 
            VALUES (?,?,?,?,?,?,?,?);
        '''
        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute(sql, (self.nome, self.sobrenome, self.usuario, self.senha, self.email, self.funcao, self.setor, self.status))
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