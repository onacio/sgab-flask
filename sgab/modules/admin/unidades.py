from flask import Blueprint, render_template, redirect, request, session
from sgab.util.auth import login_required, url_atual
from sgab.models.unidade import Unidade


admin_unidades = Blueprint('admin_unidades', __name__, url_prefix='/unidades')

@admin_unidades.route('/inserir', methods=['GET', 'POST'])
@login_required('admin')
def inserir():
    if request.method == 'POST':
        nome = request.form['nome']
        cnes = request.form['cnes']
        ine = request.form['ine']

        unidade = Unidade(nome, cnes, ine)
        unidade.inserir()

        return redirect(session['next_url'])   
        
    return redirect(session['next_url'])    

@admin_unidades.route('/listar')
@login_required('admin')
def listar():
    url_atual()

    dados = Unidade.listar_todos()    
    
    return render_template('admin/unidades/listar.html', dados=dados)

@admin_unidades.route('/excluir/<int:id_unidade>')
@login_required('admin')
def excluir(id_unidade):
    try:
        Unidade.excluir(id_unidade)        
        return redirect(session['next_url'])
    except:
        print('Erro ao excluir')
        return redirect(session['next_url'])

@admin_unidades.route('/editar/<int:id_unidade>')
@login_required('admin')
def editar(id_unidade):
    return f'página editar de unidades {id_unidade}'