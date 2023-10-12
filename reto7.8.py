def esPrimo(n):
    if n < 2:     # Si el número es menor que 2, no es primo
        return False
    i = 2         # Inicializa i en 2 ( i es el divisor )
    while i <= n**(0.5): # Mientras el divisor sea menor o igual que la raíz cuadrada de n
        if n % i == 0:   # Si el número es divisible por el divisor actual
            return False # El número no es primo
        i += 1           # Incrementar en 1 el divisor
    return True          # Si algún divisor lo divide, el número es primo

if __name__ == "__main__":
    n = 1                # Inicializa n ( primer número a comprobar ) 
    while n <= 100:      # Mientras el número sea menor o igual a 100
        if esPrimo(n):   # Si el número es primo ( se llama a la funcion esPrimo)
            print(n , end=", ") # Imprime el número en la misma línea, separado por una coma
        n += 1           # Incrementa el número a comprobar en 1 para pasar al siguiente