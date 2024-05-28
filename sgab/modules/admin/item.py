from flask import Blueprint, render_template, request, redirect, url_for, flash
from sgab.models.itens import Itens
from sgab.util.auth import login_required

admin_item = Blueprint('admin_item', __name__, url_prefix='/item')

@admin_item.route('/')
@login_required('admin')
def index():
    try:
        itens = Itens.listar_todos()        
        return render_template('admin/item.html', itens=itens)
    except Exception as erro:
        flash('Erro ao listar os itens do banco de dados', 'danger')
        raise erro

@admin_item.route('/inserir', methods=['POST'])
@login_required('admin')
def inserir():
    if request.method == 'POST':
        descricao = request.form['descricao']
        categoria = request.form['categoria']        
        status = request.form['status']        

        item = Itens(descricao, categoria, status)
        
        try:
            item.inserir()            
            flash('Item gravado com sucesso no banco', 'success')
            return redirect(url_for('admin.admin_item.index'))
        except:
            flash('Erro ao inserir o item no banco de dados, contate o administrador do sistema', 'danger')            
            return redirect(url_for('admin.admin_item.index'))