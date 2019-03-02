
import os
class Config():
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///.data/db.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOMAIN='https://domain'

    def __init__(self):
        if 'dev.py' in sys.argv:
            self.SECRET_KEY='DEBUG'
            self.DOMAIN='http://localhost:5000'
