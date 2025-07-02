from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import users, products, login, protected

app = FastAPI()

# Routes
app.include_router(users.router, prefix='/api')
app.include_router(products.router, prefix='/api')
app.include_router(login.router, prefix='/api')
app.include_router(protected.router, prefix='/api')

@app.get('/')
async def root():
    return JSONResponse(content={"mensaje": "Bienvenido a la API"})