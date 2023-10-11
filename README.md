# Reto No. 7: Bucles
Desarrolle de manera individual la mayoría de ejercicios en clase. Para cada punto cree un programa individual asimismo cree un notebook con la solución a todos los problemas. 
Al finalizar suba todo a un repo y subalo al canal reto_7 en slack, los tres primeros puntos deben incluir diagrama de flujo.

Nota: Todo el código de aquí en adelante debe ir debidamente documentado.

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado


```python
n : int = 1           # inicializa la variable n en 0
while (n <= 100) :    # mientras n sea menor o igual a 100
   print("El número " + str(n) + " elevado al cuadrado es " + str(n**2) ) # imprime el resultado del cuadrado de n
   n +=1              # incrementa el valor de n en 1

```

   
2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


```python
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
```
   

3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado


```python
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
```
   


4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.


```python
poblacionA = 25       # Población inicial del país A en millones
poblacionB = 18.9     # Población inicial del país B en millones
tasaA = 0.02          # Tasa de crecimiento anual del país A
tasaB = 0.03          # Tasa de crecimiento anual del país B
year = 2022           # Año inicial

while poblacionB <= poblacionA:        # Mientras la población del país B sea menor o igual que A
    poblacionA += poblacionA * tasaA   # Se suma la cantidad de personas segun la tasa de crecimiento anual
    poblacionB += poblacionB * tasaB   # Se suma la cantidad de personas segun la tasa de crecimiento anual
    year += 1                          # Aumenta de 1 en 1 para evaluar el crecimiento anual
    
print(f"La población del país B superará a la del país A en el año {year} con una poblacion " + str( poblacionB ) + " millones frente a una poblacion de " + str( poblacionA ) + " millones de el pais A") 
# Imprime el año en que la población de B supera a la de A
```
   


5. Imprimir el factorial de un número natural n dado.


```python

```
   


6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.


```python

```
   


7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.


```python

```
   


8.Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones


```python

```
   

