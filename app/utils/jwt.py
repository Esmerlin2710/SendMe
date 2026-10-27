
import os
from datetime import datetime, timedelta, timezone
from jose import jwt

ALGORITHM = "HS256"

SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

if not SECRET_KEY or len(SECRET_KEY) < 32:
    raise RuntimeError(
        "JWT_SECRET_KEY no está configurada correctamente"
    )


def crear_token(data: dict):
    payload = data.copy()

    payload["exp"] = (
        datetime.now(timezone.utc)
        + timedelta(hours=24)
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
