from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .core.database import engine, Base
from .routes.user_routes import router as user_routes
import logging
from contextlib import asynccontextmanager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("DB inicializada de forma correcta")
    except Exception as e:
        logger.error(f"Error al inicializar la DB: {str(e)}")
        raise
    yield
    logger.info("Aplicación finalizando...")

app = FastAPI(
    title="API de Usuario",
    description="API para la gestión de usuarios",
    version="1.0.0",
    lifespan=lifespan
)

app.middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error no manejado: {str(exc)}")
    return JSONResponse(
        content={ "mensaje" : "Error interno del servidor" },
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

app.include_router(user_routes, prefix="/api/v1")

def main():
    import uvicorn
    import webbrowser
    from threading import Timer

    host = "127.0.0.1"
    port = 8000

    def open_browser():
        webbrowser.open(f"http:{host}:{port}/docs")

    Timer(1.5, open_browser).start()

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()