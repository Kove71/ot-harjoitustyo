import sqlite3
import os

DIRNAME = os.path.dirname(__file__)

def get_connection():
    conn = sqlite3.connect(os.path.join(DIRNAME, "..", "data", "database.db"))
    conn.isolation_level = None
    return conn

def get_test_connection():
    conn = sqlite3.connect(os.path.join(DIRNAME, "..", "data", "fake_database.db"))
    conn.isolation_level = None
    return conn

