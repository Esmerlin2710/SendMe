from app.database.connection import obtener_conexion

def obtener_usuario_email(email):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, email, password_hash FROM miembros WHERE email=?", (email,))
    fetchone = cursor.fetchone()
    if not fetchone:
        cursor.execute("SELECT id, email, password_hash FROM ministerios WHERE email=?", (email,))
        fetchone = cursor.fetchone()
    return fetchone

def obtener_usuario_email_ministerio(email):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, email, password_hash FROM ministerios WHERE email=?", (email,))
    return cursor.fetchone()
    

def crear_usuario_miembro(nombre, apellido, email, password_hash, denominacion, iglesia, fecha_nacimiento):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO miembros (nombre, apellido, email, password_hash, denominacion, iglesia, fecha_nacimiento) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (nombre, apellido, email, password_hash, denominacion, iglesia, fecha_nacimiento)
    )
    conn.commit()

def crear_usuario_ministerio(nombre, apellido, email, password_hash, denominacion, iglesia, especialidad, fecha_nacimiento):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO ministerios (nombre, apellido, email, password_hash, denominacion, iglesia, especialidad, fecha_nacimiento) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (nombre, apellido, email, password_hash, denominacion, iglesia, especialidad, fecha_nacimiento)
    )
    conn.commit()