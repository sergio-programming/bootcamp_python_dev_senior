from sqlalchemy import Column, Float, String, Text, Date
from ..core.database import Base

class Project(Base): 
    __tablename__ = "projects"
    __table_args = { }
    
    proyecto_id = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(Text, nullable=False)
    presupuesto = Column(Float, nullable=False)
    fecha_inicio = Column(Date, nullable=False)