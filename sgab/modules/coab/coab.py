from flask import Blueprint, render_template, redirect, url_for
from sgab.util.auth import url_atual, login_required
from sgab.modules.coab.pedidos import coab_pedidos


coab = Blueprint('coab', __name__, url_prefix='/coab')
coab.register_blueprint(coab_pedidos)

@coab.route('/')
@login_required('user')
def index():
    url_atual()
    return render_template('coab/index.html')