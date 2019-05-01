import os
import sys

class Config:
    CWD=os.getcwd()
    DATA_PATH=os.path.join(CWD, '.data')
    UPLOAD_PATH=os.path.join(CWD, '.data/files/')

    SECRET_KEY=os.urandom(32)
    DOMAIN_SCHEMA='https'

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(CWD, '.data/db.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    DOMAIN_NAME=None
    OTP_TIMEOUT=5

    DEBUG=False

    def __init__(self):
        if all('gunicorn' not in arg for arg in sys.argv):
            self.SECRET_KEY='DEBUG'
            self.DOMAIN_NAME='localhost:5000'
            self.DOMAIN_SCHEMA='http'
            self.OTP_TIMEOUT=5
            self.DEBUG=True
        os.makedirs(self.DATA_PATH, exist_ok=True)
        os.makedirs(self.UPLOAD_PATH, exist_ok=True)
