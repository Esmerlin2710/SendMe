# 🚀 Nexelyon API - Backend

## 📌 Descripción

API desarrollada con FastAPI para el registro y autenticación de usuarios.

Incluye:

- Registro de usuarios
- Login con JWT
- Base de datos en la nube (PostgreSQL - Railway)
- Hash de contraseñas

---

## 🛠️ Tecnologías

- Python
- FastAPI
- PostgreSQL
- Railway (Base de datos en la nube)
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
```

---

## 📦 Instalación

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar el proyecto

```bash
uvicorn app.main:app --reload
```

Servidor:

```
http://127.0.0.1:8000
```

---

## 📘 Documentación automática

- Swagger:

```
http://127.0.0.1:8000/docs
```

- Redoc:

```
http://127.0.0.1:8000/redoc
```

---

## 🗄️ Base de datos

Base de datos PostgreSQL en Railway.

### Tabla `usuarios`

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    tipo_cuenta TEXT NOT NULL,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    ubicacion TEXT,
    password_hash TEXT NOT NULL
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

## 🧪 Cómo probar la API

### Opción 1: Swagger

Ir a:

```
http://127.0.0.1:8000/docs
```

---

### Opción 2: Desde frontend (React)

```javascript
fetch("http://127.0.0.1:8000/auth/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
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

---

## 🚀 Próximos pasos

- Middleware de autenticación JWT
- Protección de rutas
- Deploy del backend
- Integración completa con frontend

---

## 👨‍💻 Autor

Backend desarrollado con FastAPI para sistema Nexelyon.
