from flask import Flask, render_template, request, redirect, g, Blueprint, send_from_directory
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect

from .config import Config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config())

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


db.create_all()


if app.config['DEBUG']:
    from .models import User
    if User.query.filter_by(
        username='admin'
    ).first() is None:
        u=User(username='admin')
        u.set_password('password')
        db.session.add(u)
        db.session.commit()


if __name__ == '__main__':
    app.run(
        debug=True,
        host=host,
        port=port
    )
