from pydantic import BaseModel

class TareaEntrante(BaseModel):
    titulo: str
    descripcion: str
    
class TareaSaliente(BaseModel):
    id: int         
    titulo: str
    descripcion: str
    completada: bool    
    
# Ejemplo de un modelo para una API en produccion

class ProductoEntrante(BaseModel):
    nombre: str
    precio: float
    
class PoductoSaliente(BaseModel):
    id: int
    nombre: str
    precio: float
    disponibilidad: bool
    


