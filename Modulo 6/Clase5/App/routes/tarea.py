from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas.tarea import TareaCreate, TareaOut
from crud import tarea as crud_tarea
from database.session import get_db

router = APIRouter()

@router.post('/')
def crear(tarea: TareaCreate, db: Session = Depends(get_db)):
    return crud_tarea.crear_tarea(db, tarea)

@router.get('/', response_model=list[TareaOut])
def listar(db: Session = Depends(get_db)):
    return crud_tarea.obtener_tareas(db)


@router.get('/{tarea_id}', response_model=TareaOut)
def listar_tarea(tarea_id: int, db: Session = Depends(get_db)):   
    tarea = crud_tarea.obtener_tarea(db, tarea_id)
    if not tarea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe con ese numero de id")
    return tarea
    
@router.put('/{tarea_id}', response_model=TareaOut)
def actualizar(tarea_id: int, tarea: TareaCreate, db: Session = Depends(get_db)):
    tarea = crud_tarea.obtener_tarea(db, tarea_id)
    if not tarea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe con ese numero de id")
    
    tarea_actualizada = crud_tarea.actualizar_tarea(db, tarea_id, tarea)
    return tarea_actualizada

@router.delete('/{tarea_id}')
def eliminar(tarea_id: int, db: Session = Depends(get_db)):
    tarea = crud_tarea.obtener_tarea(db, tarea_id)
    if not tarea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe con ese numero de id")
    
    crud_tarea.eliminar_tarea(db, tarea_id)
    return JSONResponse(
        content={
            "mensaje": "Tarea eliminada exitosamente",
        },
        status_code=status.HTTP_200_OK
    )