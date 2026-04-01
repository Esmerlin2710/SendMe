from app.models.user_model import obtener_usuario_email, crear_usuario
from app.utils.security import hash_password, verificar_password
from app.utils.jwt import crear_token

def registrar_usuario(nombre, apellido, email, password, denominacion, iglesia, es_ministerio):
    user = obtener_usuario_email(email)

    if user[1]:
        return {"error": "Ese correo ya esta registrado"}
    if user:
        return {"error": "El usuario ya existe"}
    if len(password) < 8:
        return {"error": "La clave tiene que ser mayor a 8 digitos"}
    

    hashed = hash_password(password)

    try:
        crear_usuario(nombre, apellido, email, hashed, denominacion, iglesia, es_ministerio)
    except Exception as e:
        return {"error": f"Error al crear usuario: {str(e)}"}

    return {"message": "Usuario creado"}

def login_usuario(email, password):
    user = obtener_usuario_email(email)

    if not user:
        return {"error": "Credenciales incorrectas"}

    if not verificar_password(password, user[2]):
        return {"error": "Credenciales incorrectas"}

    token = crear_token({
        "user_id": user[0],
        "email": user[1]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


