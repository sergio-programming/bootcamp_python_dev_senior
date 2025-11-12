from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user_schema import UserCreate, UserLogin
from ..auth.auth_service import hash_password, verify_password

# Función para crear un usuario
def create_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if not existing_user:
        return None
    
    hashed_pw = hash_password(user.password)
    
    new_user = User(
        username=user.username,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def verify_credentials(data: UserLogin, db: Session):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not verify_password(data.password, user.password):
        return False
    return user
