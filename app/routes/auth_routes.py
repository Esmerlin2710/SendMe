from fastapi import APIRouter
from app.schemas.user_schema import RegistroMiembro, InicioUsuario, RegistroMinisterio
from app.services.auth_service import registrar_miembro, login_usuario, registrar_ministerio

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registro/miembro")
def register(data: RegistroMiembro):
    return registrar_miembro(data.nombre,
        data.apellido,
        data.email,
        data.password,
        data.denominacion,
        data.iglesia,
        data.fecha_nacimiento
        )

@router.post("/registro/ministerio")
def registro_minis(data: RegistroMinisterio):
    return registrar_ministerio(data.nombre,
        data.apellido,
        data.email,
        data.password,
        data.denominacion,
        data.iglesia,
        data.es_ministerio,
        data.especialidad,
        data.fecha_nacimiento
        )

@router.post("/login")
def login(data: InicioUsuario):
    return login_usuario(data.email, data.password)