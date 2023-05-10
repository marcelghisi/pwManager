from cryptography.fernet import Fernet
from os.path import exists

def encrypt2(enc_text):
    key = b""
    file_exists = exists('asskey.key')
    if not file_exists:
        key = Fernet.generate_key()
        with open('asskey.key', 'wb') as f:
            f.write(key)
    else:
        with open('asskey.key', 'rb') as f:
            key = f.read(10000)
    crypt = Fernet(key)
    pw = crypt.encrypt(enc_text)
    return pw

def decrypt2(enc_text):
    key = b""
    with open('asskey.key', 'rb') as f:
        key = f.read(10000)
    crypt = Fernet(key)
    pw = crypt.decrypt(enc_text)
    return pw.decode()