from flask import Flask, render_template, redirect
from sgab.modules.auth.auth import auth
from sgab.modules.coab.coab import coab

from sgab.modules.admin.admin import admin

app = Flask(__name__, template_folder='sgab/templates', static_folder='sgab/static')
app.secret_key = "fhfhfhfhfereyew"

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(coab)

@app.route('/')
def index():
    return redirect('/coab')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':        
    app.run(debug=True)

# comando do git
#git stash
#git pull
#git stash pop