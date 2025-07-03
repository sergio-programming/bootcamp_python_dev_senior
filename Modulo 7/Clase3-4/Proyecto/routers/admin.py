from fastapi import APIRouter, Depends
from auth.roles import require_role

router = APIRouter()

@router.get('/datos-admin')
def get_admin_data(current_user = Depends(require_role("admin"))):
    return {"msg": "Datos solo para administradores"}