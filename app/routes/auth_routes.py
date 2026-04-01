from fastapi import APIRouter
from app.schemas.user_schema import RegistroUsuario, InicioUsuario
from app.services.auth_service import registrar_usuario, login_usuario

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registro")
def register(data: RegistroUsuario):
    return registrar_usuario(data.nombre,
        data.apellido,
        data.email,
        data.password,
        data.denominacion,
        data.iglesia,
        data.es_ministerio
        )

@router.post("/login")
def login(data: InicioUsuario):
    return login_usuario(data.email, data.password)