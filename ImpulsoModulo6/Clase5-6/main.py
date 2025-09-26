from fastapi import FastAPI, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class RecursoBase(BaseModel):
    # los tres puntos ... indican que ese campo es obligatorio y no tiene un valor por defecto.
    nombre: str = Field(
        ..., min_length=3,
        max_length=50,
        description="Nombre del recurso",
        examples=["Mi recurso"]
    )
    descripcion: Optional[str] = Field(
        None,
        max_length=200,
        description="Descripción opcional del recurso",
        examples=["Esta es una descripción del recurso"]
    )

# Modelo para crear un recurso
class RecursoCreate(RecursoBase):
    pass

# Modelo para actualizar recursos
class RecursoUpdate(BaseModel):
    nombre: Optional[str] = Field(
        None,
        min_length=3,
        max_length=50,
        examples=["Recurso actualizado"]
    )

# Modelo para las respuestas del servidor
class RecursoResponse(RecursoBase):
    # los tres puntos ... indican que ese campo es obligatorio y no tiene un valor por defecto.
    item_id: int = Field(..., gt=0, description="ID unico del recurso") 

# Modelos para la API de usuarios
class UsuarioBase(BaseModel):
    username: str = Field(
        ...,
        min_length=4,
        max_length=16,
        description="Nombre de usuario",
        examples=["SergioPedraza"]
    )
    email: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Correo electronico valido",
        examples=["spedraza@example.com"]
    )
    edad: int = Field(
        ...,
        gt=0,
        lt=120,
        description="Edad entre 1 y 119",
        examples=["25"]
    )

# Modelo para crear usuario
class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=4, max_length=16, examples=["Actualizacion de nombre"])
    email: Optional[str] = Field(
        None,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        examples=["Actualización de email"]
    )
    edad: Optional[int] = Field(
        None,
        gt=0,
        lt=120,
        examples=["Actualización de edad"]
    )

class UsuarioResponse(UsuarioBase):
    user_id: int = Field(..., gt=0, description="Id unico del usuario")

db_recursos: List[Dict] = []
next_recurso_id = 1

db_usuarios: List[Dict] = []
next_usuario_id = 1

recursos_router = APIRouter(
    prefix="/recursos",
    tags=["Recursos"],
    responses={
        404: {"mensaje" : "Recurso no encontrado"}
    }
)

usuarios_router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    responses={
        404: {"mensaje" : "Recurso no encontrado"}
    }
)

# Endpoint de recursos (APIRest)
@recursos_router.post("/", response_model=RecursoResponse, status_code=status.HTTP_201_CREATED, summary="Crear un nuevo recurso")
async def create_recurso(recurso: RecursoCreate):
    global next_recurso_id
    new_item = recurso.model_dump()
    new_item["recurso_id"] = next_recurso_id
    db_recursos.append(new_item)
    next_recurso_id += 1
    return new_item

@recursos_router.get(
    "/",
    response_model=RecursoResponse,
    summary="Obtener todos los recursos"
)
async def get_all_recursos():
    if not db_recursos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay recursos registrados actualmente")
    return db_recursos

@recursos_router.get(
    "/{recurso_id}",
    response_model=RecursoResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener un recurso por el id"
)
async def get_recurso_by_id(recurso_id: int):
    if recurso_id < 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El id suministrado no es valido")
    for recurso in db_recursos:
        if recurso["recurso_id"] == recurso_id:
            return recurso
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe un recurso registrado con el id {recurso_id}")

@recursos_router.put(
    "/{recurso_id}",
    response_model=RecursoResponse,
    summary="Actualizamos un recurso"
)
async def update_recurso(recurso_id: int, recurso: RecursoUpdate):
    if recurso_id < 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El id suministrado no es valido")
    for recurso in db_recursos:
        if recurso["recurso_id"] == recurso_id:
            update_data = recurso.model_dump(exclude_unset=True)
            recurso.update(update_data)
            return recurso
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe un recurso registrado con el id {recurso_id}")

@recursos_router.delete(
    "/{recurso_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminacion de un recurso"
)
async def delete_recurso(recurso_id: int):
    global db_recursos
    if recurso_id < 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El id suministrado no es valido")
    for recurso in db_recursos:
        if recurso["recurso_id"] == recurso_id:
            db_recursos.remove(recurso)
            return {"mensaje" : "Recurso eliminado exitosamente"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe un recurso registrado con el id {recurso_id}")

# Endpoints de usuarios (APIRest)

@usuarios_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo usuario"
)
async def create_usuario(usuario: UsuarioCreate):
    global next_usuario_id
    new_user = usuario.model_dump()
    new_user["user_id"] = next_usuario_id
    db_usuarios.append(new_user)
    next_usuario_id += 1
    return new_user


@usuarios_router.get(
    "/",
    response_model=UsuarioResponse,
    summary="Obtener todos los usuarios"
)
async def get_all_users():
    if not db_usuarios:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay usuarios registrados actualmente")
    return db_usuarios

@usuarios_router.get(
    "/{user_id}",
    response_model=UsuarioResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener usuario por el id"
)
async def get_user_by_id(user_id: int):
    if user_id <= 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El id suministrado no es valido")
    user = next((u for u in db_usuarios if u["user_id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@usuarios_router.put(
    "/{user_id}",
    response_model=UsuarioUpdate,
    summary="Actualizar un usuario existente"
)
async def update_user(user_id: int, usuario: UsuarioUpdate):
    if user_id <= 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El id suministrado no es valido")
    user_to_update = next((u for u in db_usuarios if u["user_id"] == user_id), None)
    if not user_to_update:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    update_data = usuario.model_dump()
    user_to_update.update(update_data)
    return user_to_update

@usuarios_router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar un usuario"
)
async def delete_usuario(user_id: int):
    if user_id <= 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="El id suministrado no es valido")
    user_to_delete = next((u for u in db_usuarios if u["user_id"] == user_id), None)
    if not user_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe un usuario registrado con el id {user_id}"
        )
    db_usuarios.remove(user_to_delete)
    return {"mensaje" : f"Usuario con id {user_id} eliminado exitosamente"}

app = FastAPI(
    title="API de Recursos y Usuarios",
    description="Ejemplo de APIRest con FastAPI, APIRouter personalizados, validacion con Pydantic",
    version="1.0.0"
)

@app.get(
    "/",
    summary="Pagina principal de la aplicación APIRest"
)
async def root():
    return JSONResponse(
        content={
            "mensaje": "Bienvenido a la API de usuarios y recurso",
            "version": "1.0.0",
            "documentación": "/docs"
        },
        status_code=status.HTTP_200_OK
    )

app.include_router(usuarios_router, prefix="/api")
app.include_router(recursos_router, prefix="/api")