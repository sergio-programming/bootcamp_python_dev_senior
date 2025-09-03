from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse

usuarios = [
    {"nombre": "Sergio Pedraza", "edad": "36"},
    {"nombre": "Juanita Arboleda", "edad": "22"},
    {"nombre": "Santiago Suaza", "edad": "25"},

]

app = FastAPI()

@app.get('/')
def root():
    return JSONResponse( { "mensaje" : "Bienvenidos a la API" } ,status_code=status.HTTP_200_OK)

@app.get('/usuarios')
def getUsers():
    return JSONResponse({ "usuarios" : usuarios })