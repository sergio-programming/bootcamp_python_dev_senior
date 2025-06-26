from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.database import base, engine
from routes.user_routes import router as user_router
import logging 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="API de Usuarios",
    description="API para la gestion de usuarios con autenticacion",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Error no manejado: {str(exc)}")
    return HTTPException(
        status_code=500,
        detail="Error interno del servidor"
    )

try:
    base.metadata.create_all(bind=engine)
    logger.info("Base de datos iniciada correctamente")
except Exception as e:
    logger.error(f"Error al inicializar la base de datos: {str(e)}")
    raise

#Rutas
app.include_router(user_router, prefix='/api/v1')

