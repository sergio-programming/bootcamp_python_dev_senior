from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def catch_all_exceptions(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"Detalle": "Error interno del servidor"}
        )
    
@app.get('/')
def root():
    return{"Bienvenido": "Bienvenido a mi middleware"}

@app.get('/error')
async def generate_error():
    raise ValueError("Error intencional")


