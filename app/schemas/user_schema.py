from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, timedelta

class RegistroMinisterio(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    password: str
    denominacion: str
    iglesia: str
    es_ministerio: bool
    especialidad: str
    fecha_nacimiento: str

class RegistroMiembro(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    password: str
    denominacion: str
    iglesia: str
    fecha_nacimiento: str


class InicioUsuario(BaseModel):
    email: EmailStr
    password: str
