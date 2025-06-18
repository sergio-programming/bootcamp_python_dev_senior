from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

SECRET_KEY = "mi_clave_super_secreta"
ALGORITMO = "HS256"

"""
data = {
    "sub": "usuario",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
}

token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITMO)

print(f"Token generado: {token}")
"""

def crearToken (datos: dict, expiracion: int = 30):
    to_encode = datos.copy()
    expiracion = datetime.now(timezone.utc) +timedelta(minutes=expiracion)
    to_encode.update({"exp": expiracion})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITMO)

datos_usuario = {
    "sub": "username22",
    "role": "admin"
}

token_generado = crearToken(datos_usuario)
print(f"\nToken generado: \n{token_generado}\n")

def verificarToken(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITMO)
        return payload
    except JWTError:
        raise ValueError("Token invalido o expirado")


try:
    payload = verificarToken(token_generado)
    print(f"\nToken verificado con exito || Contenido: {payload}")
except Exception as e:
    print(f"\nError al verificar el token {e}")