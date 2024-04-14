from flask import Blueprint, request, session, redirect, url_for, render_template

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':
        session['username'] = request.form['email']
        session['senha'] = request.form['senha']
        return redirect(url_for('home.index'))
    
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():        
    session.pop('username', None)
    return redirect(url_for('home.index'))