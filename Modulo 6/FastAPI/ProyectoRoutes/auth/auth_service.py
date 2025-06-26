from passlib.context import CryptContext

#Creamos un contexto de hash para manejar las autenticaciones
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Funcion para hashear la contraseña
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)