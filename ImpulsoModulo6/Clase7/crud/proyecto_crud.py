from sqlalchemy.orm import Session
from ..models.proyecto import Project
from ..schemas.proyecto_schemas import ProyectoCreate, ProyectoUpdate

# Obtener todos los proyectos
def get_projects(db: Session):
    return db.query(Project).all()

# Obtener un proyecto
def get_project(project_id: int, db: Session):
    return db.query(Project).filter(Project.proyecto_id == project_id).first()

# Crear un proyecto
def create_project(project_data: ProyectoCreate, db: Session):
    new_project = Project(
        nombre=project_data.nombre,
        descripcion=project_data.descripcion, 
        presupuesto=project_data.presupuesto,
        fecha_inicio=project_data.fecha_inicio,
        estado=project_data.estado
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

# Actualizar un proyecto
def update_project(project_id: int, project_data: ProyectoUpdate, db: Session):
    project = db.query(Project).filter(Project.proyecto_id == project_id).first()
    if not project:
        return None
    
    if project_data.nombre is not None:
        project.nombre = project_data.nombre
    if project_data.descripcion is not None:
        project.descripcion = project_data.descripcion
    if project_data.presupuesto is not None:
        project.presupuesto = project_data.presupuesto
    if project.fecha_inicio is not None:
        project.fecha_inicio = project_data.fecha_inicio
    if project_data.estado is not None:
        project.estado = project_data.estado

    db.commit()
    db.refresh(project)
    return project

# Eliminar un proyecto
def delete_project(project_id: int, db: Session):
    project = db.query(Project).filter(Project.proyecto_id == project_id).first()
    if project:
        db.delete(project)
        db.commit()
    return project