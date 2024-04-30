from flask import Blueprint, render_template
from sgab.ext.admin.usuario import admin_usuarios


admin = Blueprint('admin', __name__, url_prefix='/admin')
admin.register_blueprint(admin_usuarios)

@admin.route('/')
def index():
    return render_template('admin/index.html')