from flask import Flask
from views.auth import auth
from views.home import home

app = Flask(__name__)
app.secret_key = "fhfhfhfhfereyew"

app.register_blueprint(auth)
app.register_blueprint(home)

app.run(debug=True)