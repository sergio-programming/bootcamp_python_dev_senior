from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from .routes.proyecto_routes import router as project_routes
from .routes.cliente_routes import router as client_routes

# Instancia de FastAPI
app = FastAPI()

# Rutas
app.include_router(project_routes, prefix="/api")
app.include_router(client_routes, prefix="/api")

# Ruta inicial
@app.get("/")
def root():
    return JSONResponse(
        content={"mensaje" : "Bienvenido a la API"},
        status_code=status.HTTP_200_OK
    )


