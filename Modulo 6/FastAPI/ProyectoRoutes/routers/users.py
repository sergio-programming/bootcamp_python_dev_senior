from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from auth.auth_service import hash_password
from models.users import User, UserUpdate 
from db.client import db_client
from routers.utils import user_schema, users_schema

# users = []

router = APIRouter()

@router.get('/users/')
async def getUsers():
    users_db = db_client.users.find()
    users = users_schema(users_db)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay usuarios registrados actualmente")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"usuarios": users})

@router.get('/users/{user_id}')
async def getUserById(user_id: int):
    user_db = db_client.users.find_one({"id": user_id})
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontro un usuario con id {user_id}")
    user = user_schema(user_db)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"usuario": user})

@router.post('/users/')
async def createUser(user: User):
    validatingUser = db_client.users.find_one({"id": user.id})
    if validatingUser:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El usuario {user.username} ya se encuentra registrado")
    hashed_password = hash_password(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    db_client.users.insert_one(user_dict)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"mensaje": f"Usuario con id {user.id} registrado exitosamente"})

@router.put('/users/{user_id}')
async def updateUser(user_id: int, user: UserUpdate):
    user_to_update = db_client.users.find_one({"id": user_id})
    if not user_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontro un usuario con id {user_id}")
    updated_user = user.dict()
    updated_user["password"] = hash_password(updated_user["password"])
    db_client.users.update_one(
        {"id": user_id},
        {"$set": updated_user}
    )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"mensaje": f"Usuario con id {user_id} actualizado exitosamente"})


@router.delete('/users/{user_id}')
async def deleteUser(user_id: int):
    user = db_client.users.find_one({"id": user_id})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontro un usuario con id {user_id}")
    db_client.users.delete_one({"id": user_id})
    return JSONResponse(status_code=status.HTTP_200_OK, content={"mensaje": f"Usuario con id {user_id} eliminado exitosamente"})

"""
@router.get('/users/')
async def getUsers():
    if not users:
        raise HTTPException(status_code=404, detail="No hay usuarios registrados actualmente")
    return JSONResponse(status_code=200, content={"usuarios": [user.dict() for user in users]})

@router.get('/users/{user_id}')
async def getUserById(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario con id {user_id}")
    return JSONResponse(status_code=200, content={"usuario": user.dict()})

@router.post('/users/')
async def createUser(user: User):
    validatingUser = next((u for u in users if u.id == user.id), None)
    if validatingUser:
        raise HTTPException(status_code=409, detail=f"Ya se encuentra un usuario registrado con el id {user.id}")
    user.password = hash_password(user.password)
    users.append(user)
    return JSONResponse(status_code=201, content={"mensaje": f"Usuario con id {user.id} registrado exitosamente"})

@router.put('/users/{user_id}')
async def updateUser(user_id: int, user: UserUpdate):
    user_to_update = next((u for u in users if u.id == user_id), None)
    if not user_to_update:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario con id {user_id}")
    user_to_update.nombre = user.nombre
    user_to_update.username = user.username
    user_to_update.password = user.password
    return JSONResponse(status_code=200, content={"mensaje": f"Usuario con id {user_id} actualizado exitosamente"})

@router.delete('/users/{user_id}')
async def deleteUser(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail=f"No se encontro un usuario con id {user_id}")
    users.remove(user)
    return JSONResponse(status_code=200, content={"mensaje": f"Usuario con id {user_id} eliminado exitosamente"})

"""