import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "postgre")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1126254560")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "tareas_db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Motor de la base de datos
engine = create_engine(
    DATABASE_URL,
    connect_args={"client_encoding": "utf8"}
)

Base = declarative_base()