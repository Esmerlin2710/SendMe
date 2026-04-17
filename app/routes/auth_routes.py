from fastapi import APIRouter
from app.schemas.user_schema import Registro, InicioUsuario
from app.services.auth_service import registro, login

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registro")
async def registro_user(data: Registro):
    return registro(data.tipo_cuenta,
        data.nombre,
        data.email,
        data.ubicacion,
        data.password,
        data.verify_password
        )


@router.post("/login")
async def login_user(data: InicioUsuario):
    return login(data.email, data.password)