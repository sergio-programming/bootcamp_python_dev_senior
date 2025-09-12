from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from routes import router


app = FastAPI()

app.include_router(router)

@app.get('/')
async def root():
    return JSONResponse({ "mensaje" : "Bienvenidos a la API de tareas" }, status_code=status.HTTP_200_OK)