# Configuracion inicial de FastAPI

# Importamos el modulo FastAPI
from fastapi import FastAPI

# Creamos una instancia de FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola mundo desde FastAPI"}