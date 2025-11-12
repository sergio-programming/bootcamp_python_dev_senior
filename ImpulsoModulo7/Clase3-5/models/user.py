from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
from ..core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), onupdate=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise ValueError("El nombre de usuario no puede estar vacio")
        if len(username) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        if len(username) > 50:
            raise ValueError("El nombre de usuario no puede tener más de 50 caracteres")
        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValueError("El username solo admite letras, números, guión y guión bajo")
        return username.lower().strip()

    @validates("password")
    def validate_password(self, key, password):
        if not password:
            raise ValueError("La contraseña no puede estar vacia")
        return password

def __repr__(self):
    return f"<User(id={self.id}, username='{self.username}')>"

def to_dict(self):
    return{
        'id': self.id,
        'username': self.username,
        'created_at': self.created_at.isoformat() if self.created_at else None,
        'updated_at': self.updated_at.isoformat() if self.updated_at else None
    }
