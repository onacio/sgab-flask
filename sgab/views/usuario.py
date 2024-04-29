from flask import Blueprint, request, session, render_template, redirect, url_for
from src.models.Usuario import Usuario

usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario.route('/inserir', methods=['GET', 'POST'])
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
        status = 1
        
        usuario = Usuario(nome, sobrenome, usuario, senha, email, funcao, setor, status)
        usuario.inserir()

    return render_template('usuario/inserir.html')

@usuario.route('/listar')
def listar():
    pass
    
    