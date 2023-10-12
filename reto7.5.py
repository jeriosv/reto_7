n = int(input("Ingrese un número natural: "))  # Declarar e inicializar con el valor dado por el usuario
factorial = 1         # Inicializar la variable factorial en 1
i : int = 1           # Inicializar la variable i en 1
while i <= n:         # Mientras que i sea menor o igual a n
    factorial *= i    # Se multiplica factorial por i cambiando sus valores con cada iteración
    i += 1            # Actualizar i para ir multiplicando por el siguiente numero
print(f"El factorial de {n} es {factorial}")  # Imprimir el factorial de n