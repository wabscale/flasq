from flask import request, redirect, url_for, flash, render_template, session, Blueprint, g
from db import get_db
from render import render
import functools
import hashlib

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

def does_user_exist(user_id):
    try:
        return get_db().execute(
            'SELECT * FROM users WHERE id = ?;',
            (user_id,)
        ).fetchone() is not None
    except:
        return False

def switch_user(user_id):
    try:
        with get_db() as db:
            username = db.execute(
                'SELECT username FROM users WHERE id = ?;',
                (user_id,)
            ).fetchone()
        if username is not None:
            g.username=username
            g.user_id=user_id
            session['username']=username
            session['user_id']=user_id
    except:
        pass

@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = sha256(request.form['password'])
        with get_db() as db:
            error = None
            res = db.execute(
                'SELECT id, username FROM users WHERE username = ? and password = ?',
                (username, password,)
            ).fetchone()
        if res is not None:
            user_id, username = res
        else:
            error = 'Incorrect username or password.'
        if error is None:
            session.clear()
            switch_user(user_id)
            return redirect(url_for('index'))
        flash(('error', error))
    return render('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    try:
        if user_id is None:
            g.username = None
            g.user_id = None
        else:
            g.user_id, g.username = get_db().execute(
                'SELECT id, username FROM users WHERE id = ?',
                (user_id,)
            ).fetchone()
    except:
        g.username = None
        g.user_id = None


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.username is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
