#Importamos FastAPI
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse

#Instanciamos la app
app = FastAPI()

class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int
    correo: EmailStr

#Lista para almacenar los usuarios
users = []

#Ruta inicial
@app.get("/")
async def read_root():
    return {"Hello": "Hola, bienvenido a la API de usuarios"}

#Ruta para crea un usuario
@app.post("/users")
async def create_user(user: User):
    if any(u.correo == user.correo for u in users):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo ya existe")
    
    users.append(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"Usuario creado": user.dict()})  
    
#Ruta para obtener todos los usuarios
@app.get("/users")
async def get_users():
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay usuarios registrados")
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Usuarios": [user.dict() for user in users]})

#Obtener un usuario por id
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Usuario": user.dict()})


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    user_to_update = next((u for u in users if u.id == user_id),None)
    if not user_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    user_to_update.nombre = user.nombre
    user_to_update.apellido = user.apellido    
    user_to_update.edad = user.edad    
    user_to_update.correo = user.correo    
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Usuario actualizado": user_to_update.dict()})
    
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    users.remove(user)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Usuario eliminado correctamente": user.dict()})