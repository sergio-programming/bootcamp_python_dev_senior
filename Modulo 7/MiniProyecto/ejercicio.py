from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from passlib.context import CryptContext
from textwrap import dedent

from usuario import Usuario

SECRET_KEY = "mi_clave_super_secreta"
ALGORITMO = "HS256"

CONTEXT_SCHEMA = "bcrypt"
pwd_context = CryptContext(schemes=[CONTEXT_SCHEMA], deprecated="auto")

usuarios = []

def crearToken(usuario: Usuario, expiracion: int = 30):
    to_encode = {
        "username": usuario.username,
        "role": usuario.role
    }
    expiracion = datetime.now(timezone.utc) +timedelta(minutes=expiracion)
    to_encode.update({"exp": expiracion})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITMO)

def registrarUsuario(username, password, role):
    
    try:
        
        if not isinstance(username, str) or not isinstance(password, str) or not isinstance(role, str):
            raise ValueError("Todos los campos deben ser de tipo String")
        
        hashed_password = pwd_context.hash(password)
    
        nuevoUsuario = Usuario(username, hashed_password, role)
    
        usuarios.append(nuevoUsuario)
    
        return f"Usuario {username} registrado exitosamente"
        
    except ValueError as e:
        print(f"Error: {e}")
      
def mostrarUsuarios():
    try:
        if not usuarios:
            raise ValueError("No hay usuarios registrados actualmente")
        
        print("\nUSUARIOS REGISTRADOS:")
        for i, usuario in enumerate (usuarios, start=1):
            print(dedent(f"""
                         Usuario #{i}
                         Username: {usuario.username}
                         Password: {usuario.password}
                         Rol: {usuario.role}
                         """))
        
    except:
      print('An exception occurred')
    
def login(username, password):
    
    try:
        
        if not isinstance(username, str) or not isinstance(password, str):
            raise ValueError("El username y el password deben ser de tipo String")
        
        user = next((u for u in usuarios if username == u.username), None)
        
        if not user:
            raise ValueError(f"No se encontro un usuario con username {username}")
        
        if not pwd_context.verify(password, user.password):
            raise ValueError("Contraseña incorrecta")        
        
        token = crearToken(user)
        
        print(f"\nEstimado {username}, bienvenido a la sesión")
        print(f"Token JWT generado: {token}")   
        
    except ValueError as e:
        print(f"Error: {e}")
    
    
def menu():
    while True:
        print()
        print("#"*30)
        print("BIENVENIDOS AL SISTEMA DE AUTENTICACIÓN")
        print("#"*30)
        print(
            dedent(f"""
                   1. Registrar usuario.
                   2. Mostrar usuarios.
                   3. Iniciar sesion.
                   4. Salir.
                   """))   
        
        try:
            
            opcion = int(input("Elija una opción: ").strip())
            
            if opcion <= 0:
                raise ValueError("La opcion debe ser un numero entero positivo")
            
            if opcion == 1:
                username = input("\nPor favor ingrese el username: ").strip()
                password = input("Por favor ingrese el password: ").strip()
                role = input("Por favor ingrese el rol: ").strip()
                
                registrarUsuario(username, password, role)
                
            elif opcion == 2:
                mostrarUsuarios()
                
            elif opcion == 3:
                username = input("\nPor favor ingrese el username: ").strip()
                password = input("Por favor ingrese el password: ").strip()
                
                login(username, password)
                
            elif opcion == 4:
                print("\nGracias por usar la aplicación")
                break
            
            else:
                print("\nLa opción ingresada no es valida")
                
        except ValueError as e:
            print(f"Error: {e}")
        
        
                     

    
