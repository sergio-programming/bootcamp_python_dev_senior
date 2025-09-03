# Respuestas personalizadas con JSONResponse
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    disponibilidad: bool
    
    
productos = [
    Producto(id=1, nombre="Portatil", precio=1000, disponibilidad=True),
    Producto(id=2, nombre="Teclado", precio=50, disponibilidad=True),
    Producto(id=3, nombre="Mouse", precio=20, disponibilidad=False),
    Producto(id=4, nombre="Monitor", precio=200, disponibilidad=True)
]    


@app.get("/productos/")
async def get_productos():
    if not productos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay productos disponibles")
    else:
        return {"Productos": productos}

@app.get("/productos/{producto_id}")
async def get_producto(producto_id: int):
    for producto in productos:
        if producto.id == producto_id:
            return producto
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    
@app.post("/productos/")
async def create_product(product: Producto):
    if product.disponibilidad:
        return JSONResponse(content={"mensaje": "Producto creado con exito", "Prodcuto": product.dict()}, status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El producto no esta disponible")
    

@app.delete("/eliminar_producto/{producto_id}")
async def delete_product(producto_id: int):
    producto = next((p for p in productos if p.id == producto_id), None)
    if producto:
        productos.remove(producto)
        return JSONResponse(content={"mensaje": "Producto eliminado con exito", "Producto": producto.dict()}, status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")