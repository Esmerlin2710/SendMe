from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"

def crear_token(data: dict):
    data_copy = data.copy()
    data_copy["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)