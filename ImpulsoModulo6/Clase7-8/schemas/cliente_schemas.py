from pydantic import BaseModel, Field, Optional, EmailStr

class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(...)
    telefono: str = Field(..., min_length=7, max_length=20)
    empresa: str = Field(..., min_length=2, max_length=100)
    direccion: str = Field(..., min_length=10, max_length=200)

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = Field(None)
    telefono: Optional[str] = Field(None, min_length=7, max_length=20)
    empresa: Optional[str] = Field(None, min_length=2, max_length=100)
    direccion: Optional[str] = Field(None, min_length=10, max_length=200)

class ClienteResponse(ClienteBase):
    cliente_id: str = Field(..., description="Id unico generado por uuid", examples="550e8400-e29b-41d4-a716-446655440000")

