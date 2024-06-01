from flask import Blueprint, request, render_template, session, redirect, url_for
from sgab.models.usuario import Usuario
from sgab.models.unidade import Unidade
from sgab.util.auth import login_required, url_atual


admin_usuarios = Blueprint('admin_usuarios', __name__, url_prefix='/usuarios')

@admin_usuarios.route('/')
@login_required('admin')
def listar():
    url_atual()
    usuarios = Usuario.listar_todos()
    unidades = Unidade.listar_todos()    

    return render_template('admin/usuarios.html', usuarios=usuarios, unidades=unidades)

@admin_usuarios.route('/inserir', methods=['GET', 'POST'])
@login_required('admin')
def inserir():    
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        usuario = request.form['usuario']
        senha = request.form['senha']
        email = request.form['email']
        funcao = request.form['funcao']
        unidade = request.form['unidade']
        status = request.form['status']
        
        usuario = Usuario(nome, sobrenome, usuario, senha, email, funcao, unidade, status)
        usuario.inserir()

        return redirect(session['next_url'])

    return render_template('admin/usuario/inserir.html')

@admin_usuarios.route('/excluir/<int:id_usuario>')
@login_required('admin')
def excluir(id_usuario):
    try:
        Usuario.excluir(id_usuario)        
        return redirect(session['next_url'])
    except:
        print('Erro ao excluir')
        return redirect(session['next_url'])
    
@admin_usuarios.route('/editar/<int:id_usuario>')
@login_required('admin')
def editar(id_usuario):
    try:
        Usuario.editar(id_usuario)        
        return redirect(session['next_url'])
    except:
        print('Erro ao editar')
        return redirect(session['next_url'])