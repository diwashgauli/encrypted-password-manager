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

def save_password(service, encrypted_password):
    conn = connect()
    conn.execute("REPLACE INTO passwords (service, password) VALUES (?, ?)", (service, encrypted_password))
    conn.commit()
    conn.close()

def fetch_password(service):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT password FROM passwords WHERE service=?", (service,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def list_services():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT service FROM passwords")
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]
