from pydantic import BaseModel, Field, Optional

class ProyectoBase(BaseModel):
    proyecto: str = Field(..., min_length=3, max_length=50)
    descripcion: str = Field(..., min_length=10, max_length=150)
    presupuesto: float = Field(..., gt=0, le=1000000000)
    fecha_inicio: str = Field(..., description="YYYY-MM-DD", examples="2025-09-25")
    estado: str = Field(..., pattern=r"^(planificacion|en_progreso|completado|cancelado)$")

class ProyectoCreate(ProyectoBase):
    pass

class ProyectoUpdate(BaseModel):
    proyecto: Optional[str] = Field(None, min_length=3, max_length=50)
    descripcion: Optional[str] = Field(None, min_length=10, max_length=150)
    presupuesto: Optional[float] = Field(None, gt=0, le=1000000000)
    fecha_inicio: Optional[str] = Field(None, description="YYYY-MM-DD", examples="2025-09-25")
    estado: Optional[str] = Field(None, pattern=r"^(planificacion|en_progreso|completado|cancelado)$")

class ProyectoResponse(ProyectoBase):
    proyecto_id: str = Field(..., description="Id unico generado por uuid", examples="550e8400-e29b-41d4-a716-446655440000")


