from pydantic import BaseModel, Field
from datetime import datetime

class TareaEntrante(BaseModel):
    titulo: str = Field(..., min_length=3)
    descripcion: str = Field(..., min_length=3)

class TareaSaliente(BaseModel):
    id: int
    fecha_creacion: datetime
    titulo: str
    descripcion: str
    completada: bool
    
    