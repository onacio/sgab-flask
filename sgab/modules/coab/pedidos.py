from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify, json
from sgab.util.auth import login_required, url_atual
from sgab.models.pedido import Pedido
from sgab.models.itens_pedidos import Itens


coab_pedidos = Blueprint('coab_pedidos', __name__, url_prefix='/pedidos')

@coab_pedidos.route('/')
@login_required('user')
def pedidos(): 
    url_atual()  
    pedidos = Pedido.listar_todos() 
    return render_template('coab/pedidos.html', pedidos=pedidos)

@coab_pedidos.route('/inserir', methods=['POST'])
@login_required('user')
def inserir():
    if request.method == 'POST':
        categoria = request.form['categoria']   
        item = request.form['item']   
        quantidade = request.form['quantidade']   
        justificativa = request.form['justificativa']   

        pedido = Pedido(
            descricao_item=item, 
            categoria=categoria, 
            quantidade=quantidade, 
            unidade_saude=session['unidade_saude'],
            justificativa=justificativa,
            )
        
        pedido.inserir()

        return redirect(url_for('coab.coab_pedidos.pedidos'))

    return 'erro'

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