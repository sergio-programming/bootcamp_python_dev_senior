## Type Hints

my_string_variable = "My String Variable"
print(f"El valor de la variable es: {my_string_variable}")
print(f"El tipo de dato de la variable es: {type(my_string_variable)}")

my_int_variable = 10
print(f"El valor de la variable es: {my_int_variable}")
print(f"El tipo de dato de la variable es: {type(my_int_variable)}")

my_float_variable = 12.5
print(f"El valor de la variable es: {my_float_variable}")
print(f"El tipo de dato de la variable es: {type(my_float_variable)}")

my_boolean_variable = False
print(f"El valor de la variable es: {my_boolean_variable}")
print(f"El tipo de dato de la variable es: {type(my_boolean_variable)}")


#El tipado de variables en Python 
from typing import Optional, List

my_typed_variable: int = "Mi variable tipada"
print(f"El valor de la variable es: {my_typed_variable}")
print(f"El tipo de dato de la variable es: {type(my_typed_variable)}")

nombres: List[int] = ["Sergio", "Luisa", "Valentina", "Jorge", "Jenifer"]
print(f"Esta es la lista de nombres: {nombres}")
print(f"El tipo de dato de la variable es: {type(nombres)}") 



