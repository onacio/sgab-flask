import sqlite3

class Conexao:
    def __init__(self):
        self.nome_banco = 'banco.db'
        self.conexao = None
        self.conectar()
        
    def conectar(self):
        """
        Estabelece uma conexão com o banco de dados SQLite especificado.

        Retorna:
            Uma conexão com o banco de dados.
        """
        try:
            self.conexao = sqlite3.connect(self.nome_banco)
            return self.conexao
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def desconectar(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.conexao:
            self.conexao.close()

    def executar_comando(self, comando):
        """
        Executa um comando SQL no banco de dados conectado.

        Argumentos:
            comando: Uma string contendo o comando SQL a ser executado.

        Retorna:
            Um cursor com os resultados da consulta ou None em caso de erro.
        """
        try:
            cursor = self.conexao.cursor()
            cursor.execute(comando)
            self.conexao.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Erro ao executar comando SQL: {e}")
            return None

