from passlib.context import CryptContext

CONTEXT_SCHEMA = "bcrypt"
pwd_context = CryptContext(schemes=[CONTEXT_SCHEMA], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

myPassword = "Metallic@88"

password_hasheado = hash_password(myPassword)
print(f"Contraseña hasheada: {password_hasheado}")

clave = input("Ingrese la contraseña: ")

if (verificar_password(clave, password_hasheado)):
    print("Acceso concedido")
else:
    print("Contraseña no es valida")