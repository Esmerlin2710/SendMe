from app.database.connection import obtener_conexion

def obtener_usuario_email(email):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, email, password_hash, es_ministerio FROM usuarios WHERE email=?", (email,))
    return cursor.fetchone()

def crear_usuario(nombre, apellido, email, password_hash, denominacion, iglesia, es_ministerio):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, apellido, email, password_hash, denominacion, iglesia, es_ministerio) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (nombre, apellido, email, password_hash, denominacion, iglesia, es_ministerio)
    )
    conn.commit()