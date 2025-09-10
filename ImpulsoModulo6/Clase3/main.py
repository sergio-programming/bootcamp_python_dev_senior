from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Optional
import uuid

app = FastAPI(
    title="API de productos",
    description="API para generar productos con FastAPI y pydantic"
)

# Modelo/Clase Base que es herencia de BaseModel
class ProductoBase(BaseModel):
    nombre: str
    precio: float

# Modelo/Clase que se usa para crear nuevos productos
class ProductoCrear(ProductoBase):
    pass

# Modelo/Clase para actualizar productos
class ProductoActualizar(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None

# Modelo/Clase para las respuestas
class ProductoRespuesta(ProductoBase):
    id: str

productos: Dict[str, dict] = {}

# Estructura del diccionario

#{
#   "msjdasj932740938420kl38" : {"nombre": "Portatil HP", "precio": 5500000}  
#}

@app.get('/')
async def root():
    return JSONResponse(content={"mensaje" : "Bienvenidos a la API de productos"}, status_code=status.HTTP_200_OK)

@app.post('/productos')
async def crear_producto(producto: ProductoCrear):
    producto_id = str(uuid.uuid4())
    nuevo_producto = producto.model_dump()
    productos[producto_id] = nuevo_producto

    return JSONResponse(content={
        "mensaje" : "Producto creado exitosamente",
        "producto" : ProductoRespuesta(id=producto_id, **nuevo_producto).model_dump()
        }, status_code=status.HTTP_201_CREATED)

@app.get('/productos/{producto_id}')
async def obtener_producto_por_id(producto_id: str):
    producto = productos.get(producto_id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe un producto con id {producto_id}")
    return JSONResponse(content={
        "producto" : ProductoRespuesta(id=producto_id, **producto).model_dump()
    }, status_code=status.HTTP_200_OK)

@app.get('/productos')
async def obtener_productos():
    if not productos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay productos registrados actualmente")
    lista_productos = [
        ProductoRespuesta(id=k, **v).model_dump() for k, v in productos.items()
    ]

    return JSONResponse(content={
        "productos" : lista_productos
    }, status_code=status.HTTP_200_OK)

@app.put('/productos/{producto_id}')
async def actualizar_producto(producto_id: str, producto: ProductoActualizar):
    producto_existente = productos.get(producto_id) 
    if not producto_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe un producto con id {producto_id}")
    producto_actualizado = {
        **producto_existente, # Desempaquetamos el diccionario actual (el que ya estaba guardado en memoria).
        **producto.model_dump(exclude_unset=True) # Desempaquetamos solo los campos enviados en la petición (los que no son None)
        }
    # {**dict1, **dict2} → en Python, cuando haces esta “desestructuración” con **,
    #  se combinan los dos diccionarios.
    # Si hay claves repetidas, las del segundo diccionario pisan las del primero.
    productos[producto_id] = producto_actualizado
    return JSONResponse(content={
        "producto" : ProductoRespuesta(id=producto_id, **producto_actualizado).model_dump()
    }, status_code=status.HTTP_200_OK)

@app.delete('/productos/{producto_id}')
async def eliminar_producto(producto_id: str):
    producto_eliminado = productos.get(producto_id)
    if not producto_eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe un producto con id {producto_id}")    
    productos.pop(producto_id)
    return JSONResponse(content={
        "mensaje" : f"El producto con id {producto_id} ha sido eliminado exitosamente",
        "producto" : ProductoRespuesta(id=producto_id, **producto_eliminado).model_dump()
    }, status_code=status.HTTP_200_OK)
