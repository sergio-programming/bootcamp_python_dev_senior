from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from models import TareaBase, TareaCrear, TareaActualizar, TareaRespuesta
from data import tareas
import uuid

router = APIRouter()

@router.get('/tareas')
async def getTasks():
    if not tareas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay tareas registradas actualmente")
    listaTareas = [
        TareaRespuesta(id=k, **v).model_dump() for k, v in tareas.items()
    ]
    return JSONResponse(
        content={ "articulos" : listaTareas },
        status_code=status.HTTP_200_OK
    )

@router.get('/tareas/{tarea_id}')
async def getTaskById(tarea_id: str):
    tarea = tareas.get(tarea_id)
    if not tarea:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No existe una tarea registrada con id {tarea_id}"
        )
    return JSONResponse(
        content={ "mensaje" : TareaRespuesta(id=tarea_id, **tarea).model_dump() },
        status_code=status.HTTP_200_OK
    )

@router.post('/tareas')
async def createTask(tarea: TareaCrear):
    tareaId = str(uuid.uuid4())
    nuevaTarea = tarea.model_dump()
    tareas[tareaId] = nuevaTarea

    return JSONResponse(
        content={ "tarea" : TareaRespuesta(id=tareaId, **nuevaTarea).model_dump()},
        status_code=status.HTTP_201_CREATED
    )

@router.put('/tareas/{tarea_id}')
async def updateTask(tarea_id: str, tarea: TareaActualizar):
    tareaExistente = tareas.get(tarea_id)
    if not tareaExistente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe una tarea registrada con id {tarea_id}")
    
    tareaActualizada = {
        **tareaExistente,
        **tarea.model_dump(exclude_unset=True)
    }

    tareas[tarea_id] = tareaActualizada

    return JSONResponse(
        content={ "tarea" : TareaRespuesta(id=tarea_id, **tareaActualizada).model_dump() },
        status_code=status.HTTP_200_OK
    )

@router.delete('/tareas/{tarea_id}')
async def deleteTask(tarea_id: str):
    tareaEliminada = tareas.get(tarea_id)
    if not tareaEliminada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No existe una tarea registrada con id {tarea_id}") 
    tareas.pop(tarea_id)
    return JSONResponse(
        content={"tarea" : TareaRespuesta(id=tarea_id, **tareaEliminada).model_dump()},
        status_code=status.HTTP_200_OK
    )