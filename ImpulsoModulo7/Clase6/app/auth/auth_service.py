from passlib.context import CryptContext

HASH_SCHEMA = "argon2"
pwd_context = CryptContext(schemes=[HASH_SCHEMA], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hash_pw: str):
    return pwd_context.verify(password, hash_pw)



