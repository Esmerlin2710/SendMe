# 🚀 Nexelyon API - Backend

## 📌 Descripción

API desarrollada con FastAPI para el registro y autenticación de usuarios.

Incluye:

- Registro de usuarios
- Login con JWT
- Base de datos en la nube (PostgreSQL - Supabase)
- Hash de contraseñas

---

## 🛠️ Tecnologías

- Python
- FastAPI
- PostgreSQL
- Supabase (Base de datos en la nube)
- psycopg2
- JWT (python-jose)
- Werkzeug (hash de contraseñas)

---

## 📁 Estructura del proyecto

```
app/
│
├── database/
│   └── connection.py
│
├── models/
│   └── user_model.py
│
├── routes/
│   └── auth_routes.py
│
├── schemas/
│   └── user_schema.py
│
├── services/
│   └── auth_service.py
│
├── utils/
│   ├── jwt.py
│   └── security.py
│
└── main.py
```

---

## ⚙️ Configuración

### 🔑 Variables de entorno

Crear un archivo `.env` en la raíz:

```
DATABASE_URL=postgresql://user:password@host:port/database

"""
Cuando creen el archvio .env copian y pegan lo de arriba y me piden la url de la base de datos porque no es esa
"""
```

---

## 📦 Instalación

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar el proyecto local

```bash
uvicorn app.main:app --reload
```

Servidor:

http://127.0.0.1:8000 --Local
https://sendme-pow6.onrender.com --Nube

---

## 📘 Documentación automática

- Swagger:

```

http://127.0.0.1:8000/docs --Local
https://sendme-pow6.onrender.com/docs --Nube

```

- Redoc:

http://127.0.0.1:8000/redoc --Local
https://sendme-pow6.onrender.com/redoc --Nube

---

## 🗄️ Base de datos

Base de datos PostgreSQL en Supabase.

### Tabla `usuarios`

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    tipo_cuenta VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔐 Autenticación

Se utiliza JWT.

- Tipo: Bearer Token
- Expiración: 24 horas

Header:

```
Authorization: Bearer <token>
```

---

## 📬 Endpoints

### 🔐 Registro

**POST** `/auth/registro`

#### Body:

```json
{
  "tipo_cuenta": "miembro",
  "nombre": "Juan",
  "email": "juan@gmail.com",
  "ubicacion": "RD",
  "password": "12345678",
  "verify_password": "12345678"
}
```

#### Respuesta:

```json
{
  "message": "Usuario creado"
}
```

#### Errores:

```json
{
  "detail": "Usuario ya existe"
}
```

---

### 🔑 Login

**POST** `/auth/login`

#### Body:

```json
{
  "email": "juan@gmail.com",
  "password": "12345678"
}
```

#### Respuesta:

```json
{
  "access_token": "token...",
  "token_type": "bearer"
}
```

---

## 🔒 Seguridad

- Contraseñas hasheadas con Werkzeug
- Validación de credenciales
- JWT para autenticación

---

## 🧠 Lógica del sistema

### Registro:

1. Verifica si el usuario existe
2. Valida contraseña
3. Hashea la contraseña
4. Guarda en la base de datos

### Login:

1. Busca usuario por email
2. Verifica contraseña
3. Genera token JWT

---

### 🔗 Conexión con Frontend

Para consumir la API desde el frontend, usar la URL:

```javascript
const API_URL = "https://sendme-pow6.onrender.com";
```

---

## 🧪 Cómo probar la API

### Opción 1: Swagger

Ir a:

```
http://127.0.0.1:8000/docs --Local
https://sendme-pow6.onrender.com/docs --Nube
```

---

### Opción 2: Desde frontend (React)

```javascript
fetch("http://127.0.0.1:8000/auth/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",         --LOCAL
  },
  body: JSON.stringify({
    email: "test@gmail.com",
    password: "12345678",
  }),
});

javascript
fetch("https://sendme-pow6.onrender.com/auth/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",         --NUBE
  },
  body: JSON.stringify({
    email: "test@gmail.com",
    password: "12345678",
  }),
});
```

---

## ⚠️ Notas importantes

- No subir `.env` a GitHub
- Usar variables de entorno en producción
- Cambiar `SECRET_KEY` en producción
- La API en la nube puede tardar unos segundos en responder si está inactiva `(modo free)`.
- No exponer credenciales en el frontend.

---

## 🚀 Próximos pasos

- Middleware de autenticación JWT
- Protección de rutas
- Deploy del backend
- Integración completa con frontend

---

## 👨‍💻 Autor

Backend desarrollado con FastAPI para sistema Nexelyon.
