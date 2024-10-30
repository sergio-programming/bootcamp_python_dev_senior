print("Tabla del 8:")
i = 1
while i < 11:
    resultado = 8 * i
    print(f"8 X {i} = {resultado}")
    i+=1

print("\nNúmeros pares del 1 al 20:")
j = 1
while j <= 20:
    if j % 2 == 0:
        print(j)
    j+=1
    
print("\nNumeros primos del 1 al 50:")
a = 2
while a <= 50:
    esPrimo = True
    if a == 2 or a == 3:
        print(a)
    else:        
        for i in range(2, a):
            if a % i == 0:
                esPrimo = False
                break
        if esPrimo:
            print(a)
    a+=1
                
                
            