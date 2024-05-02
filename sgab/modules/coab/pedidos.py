from flask import Blueprint, session, render_template, redirect, url_for
from sgab.util.auth import is_user_valid, is_user


coab_pedidos = Blueprint('coab_pedidos', __name__)

@coab_pedidos.route('/pedidos')
def pedidos():
    if is_user_valid():
        if is_user():
            return render_template('coab/pedidos.html')
        
        return redirect(url_for('admin.index'))

    return redirect(url_for('auth.logout'))