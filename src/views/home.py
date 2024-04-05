from flask import Blueprint, session, render_template, redirect, url_for
from models.pedidos_model import Pedido

home = Blueprint('home', __name__)

@home.route('/')
def index():
    print('rota inicial (/)')
    if 'username' in session:
        pedido = Pedido("Pedido de teste maior que o anterios", "Nagé", "01/01/2023")
        pedido.inserir()
        return render_template('home/index.html')
    
    
    return redirect(url_for('auth.login'))