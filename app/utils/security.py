from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str):
    return generate_password_hash(password)

def verificar_password(password: str, hashed: str):
    return check_password_hash(hashed, password)