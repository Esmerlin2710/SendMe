from pydantic import BaseModel, EmailStr

class Registro(BaseModel):
    tipo_cuenta: str
    nombre: str
    email: EmailStr
    ubicacion: str
    password: str
    verify_password: str


class InicioUsuario(BaseModel):
    email: EmailStr
    password: str
