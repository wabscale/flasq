from flask import Flask, render_template, request, redirect, g, Blueprint, send_from_directory
from auth import auth_bp, login_required, switch_user
from render import render
from db import get_db

host = '127.0.0.1'
port = 5000

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(auth_bp)

app.config.from_mapping(
    SECRET_KEY=b'SUPER_SECRET',
)

@app.route('/')
@login_required
def index():
    return render('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        host=host,
        port=port
    )
