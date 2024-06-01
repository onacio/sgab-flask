from flask import Blueprint, render_template
from sgab.modules.admin import unidades, usuarios, pedidos, item
from sgab.util.auth import login_required, url_atual
import os


admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.register_blueprint(usuarios.admin_usuarios)
admin.register_blueprint(unidades.admin_unidades)
admin.register_blueprint(pedidos.admin_pedidos)
admin.register_blueprint(item.admin_item)

@admin.route('/')
@login_required('admin')
def index():
    url_atual()
    p = os.getcwd()
    print(p)
    return render_template('admin/index.html')