import hashlib
import os

class Util:
    def generate_salt():
        return os.urandom(16)

    def generate_hash(password, salt):
         hash_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
         return hash_password
