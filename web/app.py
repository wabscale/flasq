from flask import Flask, render_template, request, redirect, g, Blueprint, send_from_directory
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect

from .config import Config

host = '0.0.0.0'
port = 5000

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

Bootstrap(app)
CSRFProtect(app)
db = SQLAlchemy(app)


# register blueprints
from .auth import auth
app.register_blueprint(auth)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        host=host,
        port=port
    )
