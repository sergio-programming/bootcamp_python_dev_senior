from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse 
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int

class ClienteIn(BaseModel):
    nombre: str
    edad: int

clientes_db: List[Cliente] = []
contador_id = 1

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"mensaje": "Bienvenido a la API"}

@app.get("/clientes", response_model=List[Cliente], status_code=status.HTTP_200_OK)
def getClientes():
    return clientes_db  # devuelve lista vacía si no hay clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente, status_code=status.HTTP_200_OK)
def getClienteById(cliente_id: int):
    cliente = next((c for c in clientes_db if c.id == cliente_id), None)
    if cliente:
        return cliente
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")

@app.post("/clientes", response_model=Cliente, status_code=status.HTTP_201_CREATED)
def createCliente(cliente: ClienteIn):
    global contador_id
    nuevo_cliente = Cliente(id=contador_id, **cliente.dict())
    clientes_db.append(nuevo_cliente)
    contador_id += 1
    return nuevo_cliente

@app.put("/clientes/{cliente_id}", response_model=Cliente, status_code=status.HTTP_200_OK)
def updateCliente(cliente_id: int, cliente: ClienteIn):
    for i, c in enumerate(clientes_db):
        if c.id == cliente_id:
            actualizado = Cliente(id=cliente_id, **cliente.dict())
            clientes_db[i] = actualizado
            return actualizado
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")

@app.delete("/clientes/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteCliente(cliente_id: int):
    for i, c in enumerate(clientes_db):
        if c.id == cliente_id:
            clientes_db.pop(i)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")