pares = []          # Crea una lista vacía para los números pares
n = int(input("Ingrese un número natural mayor o igual a 2: ")) # Declara e inicializa variable con valor dado por el usuario
# Imprime los números pares en forma descendente hasta 2
while n >= 2:       # Mientras que n sea mayor o igual a 2
    if n % 2 == 0:  # si el modulo de n es igual a 0 es par
        pares.append(n) # Se agrega a la lista de pares
        n -= 2      # se actualiza la variable disminuyendola de 2 en 2
    if n % 2 != 0:  # si el modulo de n no es igual a 0 es impar
        n-=1        # se le resta 1 para volverlo par
print("Los números pares ordenados de forma descendente: " + str(pares)) # Imprime la lista pares en forma descendente hasta 2