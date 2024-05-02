from flask import Blueprint, render_template, redirect, url_for
from sgab.modules.admin import unidades, usuarios
from sgab.util.auth import is_admin


admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.register_blueprint(usuarios.admin_usuarios)
admin.register_blueprint(unidades.admin_unidades)

@admin.route('/')
def index():
    if is_admin():
        return render_template('admin/index.html')
    
    return redirect(url_for('coab.index'))