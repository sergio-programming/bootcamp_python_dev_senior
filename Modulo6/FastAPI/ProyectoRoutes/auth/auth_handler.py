from fastapi import Depends, HTTPException, status, Request
from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/")

SECRET_KEY = "mi_clave_super_segura_y_confidencial"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 60

def create_token(data: dict, expiracion: int = ACCESS_TOKEN_EXPIRE_MINUTE):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiracion)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None
    
def get_current_user(token: str = Depends(oauth_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload