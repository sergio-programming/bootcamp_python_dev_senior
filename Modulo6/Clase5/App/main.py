from fastapi import FastAPI, HTTPException
from routes import tarea
from fastapi.responses import JSONResponse
from init_db import init_db
from database.create import crear_base_de_datos
from config import settings

app = FastAPI()

crear_base_de_datos(
    settings.DB_USER, 
    settings.DB_PASSWORD, 
    settings.DB_HOST, 
    settings.DB_NAME
)

init_db()

app.include_router(tarea.router, prefix="/tareas", tags=["Tareas"])

@app.get("/favicon.ico")
async def favicon():
    return JSONResponse(content={}, status_code=204)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de gestión de Tareas"}