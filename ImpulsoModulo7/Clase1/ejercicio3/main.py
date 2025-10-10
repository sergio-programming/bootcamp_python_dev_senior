from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(user_pw: str, hashed_pw: str):
    return pwd_context.verify(user_pw, hashed_pw)

password = "Contrasena123456"

hashed_password = hash_password(password)
print(f"Contraseña encriptada: {hash_password}")

input_password = input("\nPor favor ingrese la contraseña: ")

verify = verify_password(input_password, hashed_password)
print(f"¿La contraseña es valida?: {verify}")
