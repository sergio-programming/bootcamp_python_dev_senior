from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    nombre: str
    username: str
    password: str = Field(min_length=6)

class UserUpdate(BaseModel):
    nombre: str
    username: str
    password: str = Field(min_length=6)