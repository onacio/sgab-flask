from flask import Blueprint, render_template, redirect, url_for
from sgab.util.auth import is_user_valid, is_user
from sgab.modules.coab.pedidos import coab_pedidos


coab = Blueprint('coab', __name__, url_prefix='/coab')
coab.register_blueprint(coab_pedidos)

@coab.route('/')
def index():
    if is_user_valid():
        if is_user():
            return render_template('coab/index.html')
        
        return redirect(url_for('admin.index'))

    return redirect(url_for('auth.logout'))