from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Optional

app = FastAPI()

class Recurso(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

db: List[Dict] = []
next_item_id = 1

@app.get('/')
async def root():
    return JSONResponse(status_code=200, content={"mensaje": "Bienvenido a la API de FastAPI"})

@app.get('/recursos/')
async def get_all_recursos():
    return JSONResponse(status_code=200, content={"recursos": db})

@app.get('/recursos/{item_id}')
async def get_recurso(item_id: int):
    if item_id < 0:
        raise HTTPException(status_code=422, detail="Id invalido")
    for item in db:
        if item["item_id"] == item_id:
            return JSONResponse(status_code=200, content={"Item": item})
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

@app.post("/recursos/")
async def create_item(recurso: Recurso):
    global next_item_id
    new_item = recurso.model_dump()
    new_item["item_id"] = next_item_id
    db.append(new_item)
    next_item_id += 1

    return JSONResponse(status_code=201, content={"mensaje": new_item})