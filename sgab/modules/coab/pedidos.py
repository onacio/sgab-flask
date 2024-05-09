from flask import Blueprint, render_template, request, session, redirect, url_for
from sgab.util.auth import login_required
from sgab.models.pedido import Pedido


coab_pedidos = Blueprint('coab_pedidos', __name__, url_prefix='/pedidos')

@coab_pedidos.route('/pedidos')
@login_required('user')
def pedidos():    
    return render_template('coab/pedidos.html')

@coab_pedidos.route('/inserir', methods=['POST'])
@login_required('user')
def inserir():
    if request.method == 'POST':
        categoria = request.form['categoria']   
        item = request.form['item']   
        quantidade = request.form['quantidade']   
        justificativa = request.form['justificativa']   

        pedido = Pedido(
            categoria=categoria, 
            item=item, 
            quantidade=quantidade, 
            justificativa=justificativa,
            unidade_saude=session['unidade_saude'])
        
        pedido.inserir()

        return redirect(url_for('coab.coab_pedidos.pedidos'))

    return 'erro'