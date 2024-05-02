from flask import Blueprint, render_template, redirect, url_for, request
from sgab.util.auth import is_admin, is_user_valid
from sgab.models.unidade import Unidade


admin_unidades = Blueprint('admin_unidades', __name__, url_prefix='/unidades')

@admin_unidades.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        nome = request.form['nome']
        cnes = request.form['cnes']
        ine = request.form['ine']

        unidade = Unidade(nome, cnes, ine)
        unidade.inserir()

    if is_user_valid():
        if is_admin():
            return render_template('admin/unidades/listar.html')
        
        return redirect(url_for('coab.index'))
    
    return redirect(url_for('auth.logout'))    

@admin_unidades.route('/listar')
def listar():
    dados = Unidade.listar_todos()    
    
    return render_template('admin/unidades/listar.html', dados=dados)