from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "mi_clave_super_secreta"
ALGORITHM = "HS256"

data = {
    "sub": "Carlitos",
    "role": "admin",
    "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
}

token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

print(token)