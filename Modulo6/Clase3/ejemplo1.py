from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    edad: int
    
usuario = Usuario(nombre="Sergio", edad="36")
print(usuario)
print(f"La edad es de tipo: {type(usuario.edad)}")

usuario2 = Usuario(nombre="Andrea", edad="30")
print(usuario2)
print(f"La edad es de tipo: {type(usuario2.edad)}")