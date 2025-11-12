from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models.user import User
from ..auth.auth_handler import create_token
from ..auth.dependencies import get_current_user
from ..schemas.user_schema import UserCreate, UserLogin, UserResponse, Token, LoginResponse, Message
from ..crud.user_crud import create_user, verify_credentials

router = APIRouter()

@router.post("/login", response_model=LoginResponse, summary="Iniciar Sesión")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = verify_credentials(data, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciale inválidas"
        )
    
    token = create_token({ "sub" : data.username })

    return LoginResponse(
        access_token=token,
        token_type="bearer",
        user=UserResponse.model_validate(user)
    )

@router.post("/register", response_model=UserResponse, summary="Registrar nuevo usuario")
def create_user_route(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(user_data, db)
    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error en la solicitud de creación de usuario"
        )
    return new_user

@router.get("/me", response_model=UserResponse, summary="Obtener usuario actual")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
