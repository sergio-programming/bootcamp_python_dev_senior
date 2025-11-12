from fastapi import FastAPI, HTTPException, status, Header
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel, Field
from typing import Optional, Annotated
import secrets

HASH_SCHEME = "argon2"
SECRET_KEY = secrets.token_urlsafe(64)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 60

pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")

class RegistroData(BaseModel):
    nombre: Annotated[str, Field(min_length=3, examples=["María"])]
    username: Annotated[str, Field(min_length=8, examples=["usuario1"])]
    password: Annotated[str, Field(min_length=6, examples=[])]

class LoginData(BaseModel):
    username: Annotated[str, Field(min_length=8, examples=["usuario1"])]
    password: Annotated[str, Field(min_length=6, examples=[])]

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_pw: str) -> bool:
    return pwd_context.verify(password, hashed_pw)

def create_token(data: dict, expiration: int = ACCESS_TOKEN_EXPIRES_MINUTES):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiration)
    to_encode.update({ "exp" : expire })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

app = FastAPI()

# Database
usuarios: dict = {}

@app.get('/')
async def root():
    return JSONResponse(
        content={ "mensaje" : "Bienvenido a la API de Autenticación" },
        status_code=status.HTTP_200_OK
    )

@app.post('/register')
async def register_user(data: RegistroData):
    if data.username in usuarios:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El username proporcionado ya se encuentra registrado"
        )
    
    usuarios[data.username] = hash_password(data.password)

    return JSONResponse(
        content={ "mensaje" : f"El usuario {data.username} se ha creado exitosamente" },
        status_code=status.HTTP_201_CREATED
    )

@app.post('/login')
async def login(data: LoginData):
    user_pw = usuarios.get(data.username)
    if not user_pw or verify_password(data.password, user_pw):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    
    token = create_token({ "sub" : data.username })

    return JSONResponse(
        content={ "token" : token, "username" : data.username },
        status_code=status.HTTP_200_OK
    )

def main():
    import uvicorn
    import webbrowser
    import threading

    def abrir_navegador():
        import time
        time.sleep(1.5)
        webbrowser.open("http://localhost:8000/docs")

    threading.Thread(target="abrir_navegador", daemon=True).start()

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    main()