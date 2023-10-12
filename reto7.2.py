pares = []          # crea una lista vacía para los números pares
impares = []        # crea una lista vacía para los números impares
n : int = 1         # inicializa la variable n en 0
while (n <= 1000) : # mientras n sea menor o igual a 1000
    if n % 2 == 0 : # si el residuo de la division es igual a 0 es par
         pares.append(n)
    else:
        n % 2 != 0  # si el residuo de la division no es igual a 0 es impar
        impares.append(n)
    n +=1           # incrementa el valor de n en 1

print("Los números pares hasta 1000 son: " + str(pares)) # imprime la lista de pares
print("Los números impares hasta 1000 son: " + str(impares)) # imprime la lista de impares