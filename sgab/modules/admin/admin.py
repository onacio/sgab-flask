from flask import Blueprint, render_template
from sgab.modules.admin import unidades, usuarios
from sgab.util.auth import login_required, url_atual


admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.register_blueprint(usuarios.admin_usuarios)
admin.register_blueprint(unidades.admin_unidades)

@admin.route('/')
@login_required('admin')
def index():
    url_atual()
    return render_template('admin/index.html')