from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
import secrets

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TIME_EXPIRES = 30

def crear_token(payload: dict, expiration: int = ACCESS_TIME_EXPIRES):
    to_encode = payload.copy()
    exp = datetime.now(timezone.utc) + timedelta(minutes=expiration)
    to_encode.update({ "exp" : exp })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

token = crear_token({ "username": "spedraz7", "rol" : "admin" }, ACCESS_TIME_EXPIRES)

print(f"\nToken generado: {token}")

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        print('El token ha expirado')
        return None
    except JWTError:
        print(f"Error: Token invalido")

print(f'\nPayload: {verificar_token(token)}')