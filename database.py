import sqlite3

def connect():
    conn = sqlite3.connect("passwords.db")
    conn.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            service TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    return conn

def save_password(app_name, encrypted_password):
    conn = connect()
    conn.execute("REPLACE INTO passwords (service, password) VALUES (?, ?)", (app_name, encrypted_password))
    conn.commit()
    conn.close()
