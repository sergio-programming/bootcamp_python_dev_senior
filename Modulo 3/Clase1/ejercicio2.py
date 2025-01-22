# Manejo de excepciones especificas "Exception": no es recomendable siempre ya que puede esconder errores

def abrirArchivo():
    try:
        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())    
            print(numero)    
    except Exception as e:
        print(f"Se produjo un error: {e}")
        
abrirArchivo()