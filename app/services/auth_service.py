from app.models.user_model import obtener_usuario_email, crear_usuario
from app.utils.security import hash_password, verificar_password
from app.utils.jwt import crear_token
from fastapi import HTTPException

def registro(tipo_cuenta, nombre, email, ubicacion, password, verify_password):
    user = obtener_usuario_email(email)

    if user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="La clave tiene que ser mayor a 8 digitos")
    if password != verify_password:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")
    

    hashed = hash_password(password)

    try:
        crear_usuario(tipo_cuenta, nombre, email, ubicacion, hashed)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear usuario: {str(e)}")

    return {"message": "Usuario creado"}

def login(email, password):
    user = obtener_usuario_email(email)

    if not user:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    if not verificar_password(password, user[2]):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    token = crear_token({
        "user_id": user[0],
        "email": user[1]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


