from flask import Blueprint, request, session, redirect, url_for, render_template, flash
from sgab.db.conexao import Conexao
from sgab.models.usuario import Usuario

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():    
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
                session['status'] = dados[8]

                if dados[6] == 'Administrador':
                    return redirect(url_for('admin.index'))
            else:
                flash('Não foi possível fazer login [erro: 10]')
                #return redirect(url_for('home.index'))
                        
        else:
            flash('Usuário ou senha inválida!!!')

        return redirect(url_for('home.index'))
    
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():        
    session.pop('usuario', None)
    return redirect(url_for('home.index'))