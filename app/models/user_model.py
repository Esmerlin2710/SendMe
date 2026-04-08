from app.database.connection import obtener_conexion

def obtener_usuario_email(email):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, email, password_hash FROM usuarios WHERE email=%s", (email,))
    return cursor.fetchone()
    
    

def crear_usuario(tipo_cuenta, nombre, email, ubicacion, password_hashed):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (tipo_cuenta, nombre, email, ubicacion, password_hash) VALUES (%s, %s, %s, %s, %s)",
        (tipo_cuenta, nombre, email, ubicacion, password_hashed))
    conn.commit()