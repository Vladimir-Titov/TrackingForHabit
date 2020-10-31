import hashlib


def generate_password_hash(password: str) -> str:
    hash_password = hashlib.sha256(password.encode())
    return hash_password.hexdigest()



