from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

articulos: Dict[int, dict] = {}

class ArticuloBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float 
    impuesto: float | None = None

class CreateArticulo(ArticuloBase):
    pass

class UpdateArticulo(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    precio: float | None = None
    impuesto: float | None = None

class ResponseArticulo(ArticuloBase):
    id: int

@app.get('/')
def root():
    return JSONResponse( content={"mensaje": "Bienvenido a la API de articulos"}, status_code=status.HTTP_200_OK)

@app.get('/articulos', response_model=List[ResponseArticulo])
def getArticulos():
    if articulos:
        lista_articulos = [ResponseArticulo(id=articulo_id, **datos).model_dump() for articulo_id, datos in articulos.items()]
        return JSONResponse(content={"articulos" : lista_articulos}, status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay articulos registrados actualmente")

@app.get('/articulos/{articulo_id}', response_model=ResponseArticulo)
def getArticuloById(articulo_id: int):
    if articulo_id in articulos:
        return JSONResponse(content={"articulo": ResponseArticulo(id=articulo_id, **articulos[articulo_id]).model_dump()})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el articulo buscado")

@app.post('/articulos', response_model=ResponseArticulo)
def createArticulo(articulo: CreateArticulo):
    articulo_id = len(articulos) + 1
    articulos[articulo_id] = articulo.model_dump()
    return JSONResponse(content={"articulo" : ResponseArticulo(id=articulo_id, **articulos[articulo_id]).model_dump()})

@app.put('/articulos/{articulo_id}', response_model=ResponseArticulo)
def updateArticulo(articulo_id: int, articulo: UpdateArticulo):
    if articulo_id in articulos:
        articulo_guardado = articulos[articulo_id]
        datos_actualizados = articulo.model_dump(exclude_unset=True)
        articulo_guardado.update(datos_actualizados)
        articulos[articulo_id] = articulo_guardado

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el articulo con ese numero de id ")

@app.delete("/articulos/{articulo_id}", response_model=ResponseArticulo)
def eliminar_articulo(articulo_id):
    if articulo_id not in articulos:
        return JSONResponse(
            status_code=404,
            content={"exito": False,
                     "mensaje": "Articulo no encontrado"}
            )
    
    articulo_eliminado = articulos.pop(articulo_id)
    return JSONResponse(
        status_code=200,
        content={
            "exito": True,
            "mensaje": f"El articulo con ID {articulo_id} fue eliminado exitosamente",
            "articulo": ResponseArticulo(id=articulo_id, **articulo_eliminado). model_dump()
        }
    )