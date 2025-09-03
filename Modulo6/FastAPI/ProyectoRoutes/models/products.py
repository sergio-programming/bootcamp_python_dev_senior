from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    marca: str
    precio: int

class ProductUpdate(BaseModel):
    nombre: str
    marca: str
    precio: int