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

class Perfil(BaseModel):
    id: int
    nombre: str
    apellido: str
    email: EmailStr
    denominacion: str
    iglesia: str
    especialidad: Optional[str] = None
    descripcion: Optional[str] = None
    foto: Optional[str] = None