from app.database.connection import obtener_conexion

def obtener_usuario_email(email):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, email, password_hash FROM usuarios WHERE email=?", (email,))
    return cursor.fetchone()
    
    

def crear_usuario_miembro(nombre, apellido, email, password_hash, denominacion, iglesia, fecha_nacimiento):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, apellido, email, password_hash, denominacion, iglesia, fecha_nacimiento) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (nombre, apellido, email, password_hash, denominacion, iglesia, fecha_nacimiento)
    )
    conn.commit()

def crear_usuario_ministerio(username, email, password_hash, denominacion, iglesia, es_ministerio, especialidad, fecha_nacimiento):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (username, email, password_hash, denominacion, iglesia, es_ministerio, especialidad, fecha_nacimiento) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (username, email, password_hash, denominacion, iglesia, es_ministerio, especialidad, fecha_nacimiento)
    )
    conn.commit()