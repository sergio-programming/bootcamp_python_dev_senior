from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from auth.auth_service import verify_password
from routers.users import users
from auth.auth_handler import create_token

class Login(BaseModel):
    username: str
    password: str

router = APIRouter()

@router.post('/')
def loginUser(data: Login):
    user = next((u for u in users if u.username == data.username), None)
    if not user:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario {data.username} registrado")
    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta. Acceso no autorizado")
    token = create_token({"id": user.id, "username": user.username})
    return JSONResponse(
        status_code=200,
        content={
            "mensaje": f"Bienvenido {user.username}, acceso concedido",
            "token": token,
            "token_type": "bearer"
        }
    )
