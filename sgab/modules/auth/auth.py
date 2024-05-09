from flask import Blueprint, request, session, redirect, url_for, render_template, flash
from sgab.db.conexao import Conexao
from sgab.models.usuario import Usuario
from sgab.util.auth import url_atual

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    url_atual()   
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute('SELECT * FROM usuarios WHERE usuario = ? AND senha = ?', (usuario, senha))
        dados = cur.fetchone()

        if dados:            
            if dados[8] == 1:
                session['nome'] = dados[1]
                session['usuario'] = dados[3]            
                session['cargo'] = dados[6] 
                session['unidade_saude'] = dados[7]        
                session['status'] = dados[8]

                session.permanent = True

                if dados[6] == 'admin':
                    return redirect(url_for('admin.index'))
            else:
                flash('Não foi possível fazer login [erro: 10]')                
                        
        else:
            flash('Usuário ou senha inválida!!!')

        return redirect(url_for('coab.index'))
    
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():    
    url_atual()    
    session.pop('nome', None)
    session.pop('usuario', None)
    session.pop('cargo', None)
    session.pop('status', None)
    return redirect(url_for('auth.login'))