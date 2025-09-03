from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.login import Login
from db.client import db_client
from auth.auth_service import verify_password
from auth.auth_handler import create_token

router = APIRouter()

@router.post('/login/')
def loginUser(data: Login):
    user = db_client.users.find_one({"username": data.username})
    if not user:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario {data.username} registrado")
    if not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta. Acceso no autorizado")
    token = create_token({"id": user["id"], "username": user["username"]})
    return JSONResponse(
        status_code=200,
        content={
            "mensaje": f"Bienvenido {user["username"]}, acceso concedido",
            "token": token,
            "token_type": "bearer"
        }
    )
