""""
Los operadores logicos sirven para realizar comparaciones entre dos o mas expresiones
Conjunción (y): and
Disyunción (o): or 
Negación: not
"""

a = 12
b = 16
c = 10
d = 14
e = 16

comparacion1 = a < d and b == e
comparacion2 = a > b and b == e
comparacion3 = a <= c or d == c
comparacion4 = b >= d or b != e
comparacion5 = not(b == e)
comparacion6 = not(a == d)

print(f"¿{a} es menor que {d} y {b} es igual a {e}?: {comparacion1}")
print(f"¿{a} es mayor que {b} y {b} es igual a {e}?: {comparacion2}")
print(f"¿{a} es menor igual que {c} o {d} es igual a {c}?: {comparacion3}")
print(f"¿{b} es mayor igual que {d} o {b} es diferente a {e}?: {comparacion4}")
print(f"¿No es {b} igual que {e}?: {comparacion5}")
print(f"¿No es {a} igual que {d}?: {comparacion6}")