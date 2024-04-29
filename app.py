from flask import Flask
from src.views.auth import auth
from src.views.home import home
from src.views.usuario import usuario

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
app.secret_key = "fhfhfhfhfereyew"

app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(usuario)

if __name__ == '__main__':
    app.run(debug=True)

#set FLASK_ENV=development
#git stash
#git pull
#git stash pop