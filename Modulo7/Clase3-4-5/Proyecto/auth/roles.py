from fastapi import Depends, HTTPException, status
from auth.security import get_current_user

def require_role(require_role: str):
    def role_dependency(user: dict = Depends(get_current_user)):
        if user["role"] != require_role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acceso denegado")
        return user
    return role_dependency




