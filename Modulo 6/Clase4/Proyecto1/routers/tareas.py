from datetime import datetime
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import TareaEntrante, TareaSaliente

router = APIRouter()

tareas = []
id_actual = 1

@router.post("/tareas", response_model=TareaSaliente)
async def crear_tarea(tarea: TareaEntrante):
    global id_actual
    nueva_tarea = {
        "id": id_actual,
        "fecha_creacion": datetime.now(),
        "titulo": tarea.titulo,
        "descripcion": tarea.descripcion,
        "completada": False
    }
    tareas.append(nueva_tarea)
    id_actual += 1
    return JSONResponse(content={"tarea": jsonable_encoder(nueva_tarea)}, status_code=status.HTTP_201_CREATED)

@router.get("/tareas", response_model=list[TareaSaliente])
async def obtener_tareas():
    if tareas:
        return JSONResponse(content={"tareas": jsonable_encoder(tareas)}, status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron tareas registradas")
    
    