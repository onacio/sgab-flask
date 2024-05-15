from flask import Blueprint, request, render_template, session, redirect, flash
from sgab.util.auth import login_required, url_atual
from sgab.models.pedido import Pedido
from datetime import datetime


admin_pedidos = Blueprint('admin_pedidos', __name__, url_prefix='/pedidos')

@admin_pedidos.route('/')
@login_required('admin')
def listar():
    url_atual()    
    pedidos = Pedido.listar_todos()   
    if pedidos == None:
        return render_template('admin/pedidos-listar.html', pedidos=False)
    else:
        return render_template('admin/pedidos-listar.html', pedidos=pedidos)
    

@admin_pedidos.route('/atender', methods=['POST'])
@admin_pedidos.route('/atender/<int:id_pedido>')
@login_required('admin')
def atender_pedido(id_pedido=''):
    if request.method == 'POST':     
        id_pedido = request.form['id']
        quantidade = request.form['quantidade-liberada']
        status = 1
        data = datetime.now().strftime("%d/%m/%Y")

        try:
            Pedido.alterar(id_pedido, quantidade, status, data) 
            flash('Pedido atendido com sucesso!!!', 'success')
            return redirect(session['next_url'])  
        except:
            flash('Erro ao atender o pedido', 'danger')
            return redirect(session['next_url'])
    
    pedido = Pedido.listar_um(id_pedido)          
    return render_template('admin/pedido-atender.html', pedido=pedido)    



@admin_pedidos.route('/inserir', methods=['GET', 'POST'])
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
        
        # usuario = Usuario(nome, sobrenome, usuario, senha, email, funcao, unidade, status)
        # usuario.inserir()

        return redirect(session['next_url'])

    return render_template('admin/usuario/inserir.html')

@admin_pedidos.route('/excluir/<int:id_usuario>')
@login_required('admin')
def excluir(id_usuario):
    try:
        # Usuario.excluir(id_usuario)        
        return redirect(session['next_url'])
    except:
        print('Erro ao excluir')
        return redirect(session['next_url'])
    
@admin_pedidos.route('/editar/<int:id_usuario>')
@login_required('admin')
def editar(id_usuario):
    try:
        # Usuario.editar(id_usuario)        
        return redirect(session['next_url'])
    except:
        print('Erro ao editar')
        return redirect(session['next_url'])
