from sqlalchemy.orm import Session
from ..models.cliente import Client
from ..schemas.cliente_schemas import ClienteCreate, ClienteUpdate

# Obtener todos los clientes
def get_clients(db: Session):
    return db.query(Client).all()

# Obtener un cliente
def get_client(cliente_id: int, db: Session):
    return db.query(Client).filter(Client.cliente_id == cliente_id).first()

# Crear un nuevo cliente
def create_client(cliente_data: ClienteCreate, db: Session):
    new_client = Client(
        nombre=cliente_data.nombre,
        email=cliente_data.email,
        telefono=cliente_data.telefono,
        empresa=cliente_data.empresa,
        direccion=cliente_data.direccion
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

# Actualizar un cliente
def update_client(cliente_id: int, cliente_data: ClienteUpdate, db: Session):
    client = db.query(Client).filter(Client.cliente_id == cliente_id).first()
    if not client:
        return None
    
    if cliente_data.nombre:
        client.nombre = cliente_data.nombre
    if cliente_data.email:
        client.email = cliente_data.email
    if cliente_data.telefono:
        client.telefono = cliente_data.telefono
    if cliente_data.empresa:
        client.empresa = cliente_data.empresa
    if cliente_data.direccion:
        client.direccion = cliente_data.direccion

    db.commit()
    db.refresh(client)
    return client

# Eliminar un cliente
def delete_client(cliente_id: int, db: Session):
    client = db.query(Client).filter(Client.cliente_id == cliente_id).first()
    if not client:
        return None
    
    db.delete(client)
    db.commit()
    return client