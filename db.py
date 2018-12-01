import sqlite3
import os

DN_NAME='database.db'

def get_db():
    return sqlite3.connect(DB_NAME)
