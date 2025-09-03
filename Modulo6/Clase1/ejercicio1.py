# Instalacion de FastAPI y uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Cliente(BaseModel):
    nombre: str
    apellido: str
    edad: int
    
@app.post("/clientes")
def crearCliente(cliente: Cliente):
    return {"mensaje": f"Cliente {cliente.nombre} creado con exito"}


@app.get("/")
def inicio():
    return {"mensaje": "Hola mundo"}

inicio()