# Instalacion de pydantic
from pydantic import BaseModel, Field

# Ejemplos de uso de Field en los modelos

class Usuario(BaseModel):
    username: str = Field(..., min_length=3, max_length=15) 
    edad: int = Field(..., gt=0, lt=100)
    
class Reserva(BaseModel):
    cliente: str = Field(..., min_length=3)  
    fecha: str = Field(..., pattern="^\d{4}-\d{2}-\d{2}$") #AAAA-MM-DD
    cantidad_personas: int = Field(..., gt=0, lt=10)
    
reserva = Reserva(cliente="Juan", fecha="2025-01-28", cantidad_personas="5")
print(reserva)
print(f"El tipo de dato de la variable fecha es: {type(reserva.fecha)}")
print(f"El tipo de dato de la variable cantidad_personas es: {type(reserva.cantidad_personas)}")