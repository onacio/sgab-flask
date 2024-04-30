from flask import Blueprint, request, render_template, session, redirect, url_for
from sgab.models.usuario import Usuario
from sgab.db.conexao import Conexao


admin_usuarios = Blueprint('admin_usuarios', __name__, url_prefix='/usuario')

@admin_usuarios.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if not 'usuario' in session:
        return redirect(url_for('auth.login'))        
    
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        usuario = request.form['usuario']
        senha = request.form['senha']
        email = request.form['email']
        funcao = request.form['funcao']
        setor = request.form['setor']
        status = request.form['status']
        
        usuario = Usuario(nome, sobrenome, usuario, senha, email, funcao, setor, status)
        usuario.inserir()

    return render_template('admin/usuario/inserir.html')

@admin_usuarios.route('/listar')
def listar():
    con = Conexao().conectar()
    cur = con.cursor()
    cur.execute('SELECT * FROM usuarios')
    dados = cur.fetchall()    
    con.close()

    return render_template('admin/usuario/listar.html', dados = dados)

@admin_usuarios.route('/excluir')
def excluir():
    return render_template('admin/usuario/inserir.html')

@admin_usuarios.route('/relatorio')
def relatorio():
    return render_template('admin/usuario/relatorio.html')