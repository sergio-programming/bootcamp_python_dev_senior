from fastapi import APIRouter, HTTPException, Depends
from auth.auth_handler import get_current_user

router = APIRouter()

@router.get('/')
def get_profile(user_data: dict = Depends(get_current_user)):
    return {
        "mensaje": f"Hola {user_data['username']}, este es tu perfil privado 🕵️‍♂️",
        "usuario": user_data
    }
