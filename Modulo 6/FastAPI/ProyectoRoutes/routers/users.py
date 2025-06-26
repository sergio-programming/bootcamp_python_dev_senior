from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from auth.auth_service import hash_password

class User(BaseModel):
    id: int
    nombre: str
    username: str
    password: str = Field(min_length=6)

class UserUpdate(BaseModel):
    nombre: str
    username: str
    password: str = Field(min_length=6)

users = []

router = APIRouter()

@router.get('/')
async def getUsers():
    if not users:
        raise HTTPException(status_code=404, detail="No hay usuarios registrados actualmente")
    return JSONResponse(status_code=200, content={"usuarios": [user.dict() for user in users]})

@router.get('/{user_id}')
async def getUserById(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario con id {user_id}")
    return JSONResponse(status_code=200, content={"usuario": user.dict()})

@router.post('/')
async def createUser(user: User):
    validatingUser = next((u for u in users if u.id == user.id), None)
    if validatingUser:
        raise HTTPException(status_code=409, detail=f"Ya se encuentra un usuario registrado con el id {user.id}")
    user.password = hash_password(user.password)
    users.append(user)
    return JSONResponse(status_code=201, content={"mensaje": f"Usuario con id {user.id} registrado exitosamente"})

@router.put('/{user_id}')
async def updateUser(user_id: int, user: UserUpdate):
    user_to_update = next((u for u in users if u.id == user_id), None)
    if not user_to_update:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario con id {user_id}")
    user_to_update.nombre = user.nombre
    user_to_update.username = user.username
    user_to_update.password = user.password
    return JSONResponse(status_code=200, content={"mensaje": f"Usuario con id {user_id} actualizado exitosamente"})

@router.delete('/{user_id}')
async def deleteUser(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario con id {user_id}")
    users.remove(user)
    return JSONResponse(status_code=200, content={"mensaje": f"Usuario con id {user_id} eliminado exitosamente"})

