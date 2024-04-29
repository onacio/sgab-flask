from src.services.conexao import Conexao
from flask import session

def verificar_login(usuario, senha):        
    con = Conexao().conectar()
    cur = con.cursor()
    cur.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (usuario, senha))
    dados = cur.fetchone()
        
    if dados:
        return dados
    else:
        return False

def esta_autenticado():
    if 'usuario' in session:
        return 'Está autenticado'