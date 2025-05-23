import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

def crear_base_de_datos(nombre, usuario, password, host="localhost"):
    try:
        conexion = psycopg2.connect(
            dbname="postgres",
            user=usuario,
            password=password,
            host=host,
            port="5432",
            client_encoding="utf8"
        )
        
        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        cursor = conexion.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (nombre,))
        
        if not cursor.fetchone():
            cursor.execute(sql.SQL("CREATE DATABASE {} ENCODING 'UTF8'").format(sql.Identifier(nombre)))
            print(f"Base de datos {nombre} creada exitosamente.")
        else:
            print(f"Base de datos {nombre} ya existe")
            
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        if cursor in locals(): cursor.close()
        if conexion in locals(): conexion.close()