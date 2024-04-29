from flask import Blueprint, session, render_template, redirect, url_for


home = Blueprint('home', __name__)

@home.route('/')
def index():    
    if 'username' in session:        
        return render_template('home/index.html')
    
    return redirect(url_for('auth.login'))

@home.route('/sobre')
def sobre():    
    if 'username' in session:        
        return render_template('home/sobre.html')
    
    return redirect(url_for('auth.login'))