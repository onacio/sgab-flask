from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from sgab.util.auth import login_required, url_atual
from sgab.models.pedido import Pedido
from sgab.models.itens import Itens

coab_pedidos = Blueprint('coab_pedidos', __name__, url_prefix='/pedidos')

@coab_pedidos.route('/')
@login_required('user')
def index(): 
    url_atual()  
    pedidos = Pedido.listar_todos()
    if pedidos == None:
        return render_template('coab/pedidos.html', pedidos=False) 
    else:
        return render_template('coab/pedidos.html', pedidos=pedidos)

@coab_pedidos.route('/inserir', methods=['GET', 'POST'])
@login_required('user')
def inserir():
    if request.method == 'POST':
        categoria = request.form['categoria']   
        item = request.form['item']   
        quantidade = request.form['quantidade']   
        justificativa = request.form['justificativa']  

        try:
            pedido = Pedido(
                descricao=item, 
                categoria=categoria, 
                solicitante=session['unidade_saude'],
                quantidade=quantidade.lstrip(), 
                quantidade_liberada='',
                justificativa=justificativa)
            
            pedido.inserir()
            flash('Pedido realizado com sucesso!!!', 'success')
            return redirect(url_for('coab.coab_pedidos.index'))
        except Exception as erro:
            flash('Erro ao fazer pedido', 'danger')
            raise erro 

    return redirect(session['next_url'])

@coab_pedidos.route('/excluir/<int:id_pedido>')
@login_required('user')
def excluir(id_pedido):    
    try:
        Pedido.excluir(id_pedido)
        return redirect(session['next_url'])
    except:
        print('')

@coab_pedidos.route('/listar/<categoria>')
@login_required('user')
def listar_categoria(categoria):
    cat = Itens.listar_categoria(categoria)
    return jsonify(cat)