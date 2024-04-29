from flask import Blueprint, request, session, redirect, url_for, render_template, flash
from sgab.ext.db.conexao import Conexao

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':
        usuario = request.form['email']
        senha = request.form['senha']

        con = Conexao().conectar()
        cur = con.cursor()
        cur.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (usuario, senha))
        dados = cur.fetchone()

        if dados:
            session['nome'] = dados[1]
            session['usuario'] = dados[3]
            session['email'] = dados[5]
            session['cargo'] = dados[6]
            session['status'] = dados[8]
        else:
            flash('Usuário ou senha inválida!!!')
                
        return redirect(url_for('home.index'))
    
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():        
    session.pop('usuario', None)
    return redirect(url_for('home.index'))