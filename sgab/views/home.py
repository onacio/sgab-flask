from flask import Blueprint, session, render_template, redirect, url_for, flash


home = Blueprint('home', __name__)

@home.route('/')
def index():        
    if 'usuario' in session:
        return render_template('home/index.html')
    
    return redirect(url_for('auth.login'))

@home.route('/sobre')
def sobre():    
    if not 'usuario' in session:        
        return redirect(url_for('auth.login'))
        
    return render_template('home/sobre.html')  