from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    LocalSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Base = declarative_base()
except SQLAlchemyError as e:
    raise Exception(f"Error al conectar con la base de datos: {str(e)}")

def get_db():
    db = LocalSession()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error en la operación de base de datos: {str(e)}")
    finally:
        db.close()