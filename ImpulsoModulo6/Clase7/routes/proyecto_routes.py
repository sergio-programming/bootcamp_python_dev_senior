from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..schemas.proyecto_schemas import ProyectoCreate, ProyectoUpdate, ProyectoResponse
from ..crud.proyecto_crud import get_projects, get_project, create_project, update_project, delete_project

router = APIRouter(prefix="/projects", tags=["Projects"])

# Endpoint para obtener los proyectos
@router.get("/", response_model=ProyectoResponse)
def get_users_route(db: Session = Depends(get_db)):
    projects = get_projects(db)
    if not projects:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encuentran proyectos registrados actualmente"
        )
    return projects

# Endpoint para obtener un proyecto
@router.get("/{project_id}", response_model=ProyectoResponse)
def get_user_route(project_id: int, db: Session = Depends(get_db)):
    project = get_project(project_id, db)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encuentra un proyecto registrado con el id {project_id}"
        )
    return project

# Endpoint para crear un proyecto
@router.post("/", response_model=ProyectoResponse)
def create_project(project: ProyectoCreate, db: Session = Depends(get_db)):
    new_project = create_project(project, db)
    if not new_project:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al crear el proyecto"
        )
    return new_project

# Endpoint para actualizar un proyecto
@router.patch("/{project_id}", response_model=ProyectoResponse)
def update_project_route(project_id: int, project: ProyectoUpdate, db: Session = Depends(get_db)):
    project_to_update = update_project(project_id, project, db)
    if not project_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encuentra un proyecto registrado con el id {project_id}"
        )
    return project_to_update

# Endpoint para eliminar un proyecto
@router.delete("/{project_id}", response_model=ProyectoResponse)
def delete_project_route(project_id: int, db: Session = Depends(get_db)):
    project_to_delete = delete_project(project_id, db)
    if not project_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encuentra un proyecto registrado con el id {project_id}"
        )
    return JSONResponse(
        content={"mensaje" : f"El proyecto con id {project_id} ha sido eliminado exitosamente"},
        status_code=status.HTTP_200_OK
    )
