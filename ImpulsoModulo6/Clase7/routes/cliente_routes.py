from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..core.database import get_db
from ..schemas.cliente_schemas import ClienteCreate, ClienteUpdate, ClienteResponse
from ..crud.cliente_crud import get_clients, get_client, create_client, update_client, delete_client

router = APIRouter(prefix="/clients", tags=['Clientes'])

# Endpoint para obtener todos los clientes
@router.get("/", response_model=list[ClienteResponse])
def get_clients_route(db: Session = Depends(get_db)):
    try:
        clients = get_clients(db)
        if not clients:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No se encuentran clientes registrados actualmente"
            )    
        return clients
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de bases de datos: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {e}"
        )
    
# Endpoint para un obtener un cliente
@router.get("/{cliente_id}", response_model=ClienteResponse)
def get_client_route(cliente_id: int, db: Session = Depends(get_db)):
    try:
        client = get_client(cliente_id, db)
        if not client:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encuentra un cliente registrado con el id {cliente_id}"
            )
        return client
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de base de datos: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {e}"
        )

# Endpoint para crear un cliente   
@router.post("/", response_model=ClienteResponse)
def create_client_route(cliente: ClienteCreate, db: Session = Depends(get_db)):
    try:
        new_client = create_client(cliente, db)
        if not new_client:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error al crear el cliente"
            )
        return new_client
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de base de datos: {e}"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {e}"
        )
    
# Endpoint para actualizar un cliente
@router.patch("/{cliente_id}", response_model=ClienteResponse)
def update_client_route(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    try:
        client_to_update = update_client(cliente_id, cliente, db)
        if not client_to_update:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encuentra un cliente registrado con el id{cliente_id}"
            )
        return client_to_update
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de base de datos: {e}"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {e}"
        )
    
# Endpoint para eliminar un cliente
@router.delete("/{cliente_id}", response_model=ClienteResponse)
def delete_client_route(cliente_id: int, db: Session = Depends(get_db)):
    try:
        client_to_delete = delete_client(cliente_id, db)
        if not client_to_delete:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"No se encuentra un cliente registrado con el id{cliente_id}"
            )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error de base de datos: {e}"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {e}"
        )