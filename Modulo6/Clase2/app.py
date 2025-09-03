from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional     

# Crear la instancia de FastAPI
app = FastAPI()

#Lista para almacenar los items
items = []

# Modelo de Pydantic para crear y validar los items
class Item(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    impuesto: Optional[float] = None
    
    
@app.get("/")
def root():
    return {"Mensaje": "Bienvenidos a la API de Items"}
    
@app.get("/items/")
def get_all_items():
    if not items:
        raise HTTPException(status_code=404, detail="No hay items")
    return {"Items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="El item no existe") 
    return {"Item_id": item_id, "item": items[item_id]}

@app.post("/items/")
def create_items(item: Item):
    items.append(item)
    item_id = len(items) - 1
    return {"Mensaje": "Item creado con éxito", "item_id": item_id, "Item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="El item no existe") 
    items[item_id] = item
    return{"Mensaje": "Item actualizado con exito", "item_id": item_id, "Item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="El item no existe") 
    del items[item_id]
    return{"Mensaje": "Item eliminado con exito", "item_id": item_id}