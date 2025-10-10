from jose import jwt
from datetime import datetime, timezone, timedelta
import secrets

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = 'HS256'

def main():
    data = {
        "subject" : "usuario123",
        "exp" : datetime.now(timezone.utc) + timedelta(minutes=30) 
    }

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    print("Token JWT generado")
    print(f'\n{token}')

if __name__ == '__main__':
    main()