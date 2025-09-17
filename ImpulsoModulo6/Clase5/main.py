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
