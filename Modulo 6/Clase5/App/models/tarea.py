from sqlalchemy import Column, Integer, String, Boolean
from database.base import Base

class Tarea (Base):
    
    __tablename___ = "tareas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    completado = Column(Boolean, default=False)
    
