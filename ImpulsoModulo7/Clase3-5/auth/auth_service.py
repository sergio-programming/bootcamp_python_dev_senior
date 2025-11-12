from passlib.context import CryptContext

HASH_SCHEME = "argon"

pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_pw: str):
    return pwd_context.verify(password, hashed_pw)