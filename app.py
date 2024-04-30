from flask import Flask
from sgab.ext.auth.auth import auth
from sgab.ext.site.home import home

from sgab.ext.admin.admin import admin

app = Flask(__name__, template_folder='sgab/templates', static_folder='sgab/static')
app.secret_key = "fhfhfhfhfereyew"

app.register_blueprint(auth)
app.register_blueprint(home)

app.register_blueprint(admin)

if __name__ == '__main__':    
    app.run(debug=True)

# comando do git
#git stash
#git pull
#git stash pop