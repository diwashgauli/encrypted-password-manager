from cryptography.fernet import Fernet
import os

def get_key():
    if not os.path.exists("keys"):
        os.mkdir("keys")
    if not os.path.exists("keys/key.key"):
        key = Fernet.generate_key()
        with open("keys/key.key", "wb") as f:
            f.write(key)
    with open("keys/key.key", "rb") as f:
        return f.read()

def get_encryptor():
    key = get_key()
    return Fernet(key)
