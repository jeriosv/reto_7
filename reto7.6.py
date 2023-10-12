print("Piense y memorice un número a adivinar entre 1 y 100")  # Información
minimo : int = 1          # Inicializar las variables para la búsqueda  
maximo : int = 100
i : int = 0
while minimo <= maximo:   # Mientras el minimo sea menor o igual que el maximo
    i += 1                # Incrementar el contador de intento
    medio = (minimo + maximo) // 2 # Adivinar el número medio del rango actual redondeado hacia abajo
    respuesta = input(f"¿Es {medio} el número? (s/n) ")
    
    if respuesta == "s":  # Actualizar el rango de búsqueda según la respuesta
        print(f"¡Adiviné el número en {i} intentos!")
        break
    elif respuesta == "n":
        respuesta = input(f"¿Es el número mayor o menor que {medio}? (Digite 1=Mayor o 2=Menor) ")
        if respuesta == "1":
            minimo = medio + 1
        elif respuesta == "2":
            maximo = medio - 1
        else:
            print("Respuesta inválida, intente de nuevo.")
    else:
        print("Respuesta inválida, intente de nuevo.")