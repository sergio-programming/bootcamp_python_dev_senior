from sqlalchemy import Column, String
from ..core.database import Base


class Client(Base):
    __tablename__ = "clients"

    cliente_id = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, nullable=False)
    empresa = Column(String, nullable=False)
    direccion = Column(String, nullable=False)


    