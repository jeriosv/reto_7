n = int(input("Ingrese un número de 2 a 50: ")) # Declarar e inicializar con el valor dado por el usuario
i : int = 1          # Inicializar la variable i en 1
while i <= n :       # Mientras i sea menor o igual n
    if n%i == 0 :  # Si n es divisible por i su residuo es igual a 0
        print(f"{i} es divisor de {n}")   # Imprimir i
    i +=1          # Actualizar i en 1 más