from pydantic import BaseModel, EmailStr
from typing import Optional

class RegistroUsuario(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    password: str
    denominacion: str
    iglesia: str
    es_ministerio: bool
    especialidad: Optional[str] = None
    descripcion: Optional[str] = None



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
    es_ministerio: bool
    especialidad: Optional[str] = None
    descripcion: Optional[str] = None
    foto: Optional[str] = None