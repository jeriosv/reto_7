poblacionA = 25000000   # Población inicial del país A
poblacionB = 18900000   # Población inicial del país B
tasaA = 0.02          # Tasa de crecimiento anual del país A
tasaB = 0.03          # Tasa de crecimiento anual del país B
year = 2022           # Año inicial

while poblacionB <= poblacionA:      # Mientras la población del país B sea menor o igual que A
    poblacionA *= ( 1 + tasaA )      # Se suma la cantidad de personas segun la tasa de crecimiento anual
    poblacionB *= ( 1 + tasaB )      # Se suma la cantidad de personas segun la tasa de crecimiento anual
    year += 1                        # Aumenta el año
    
print(f"La población del país B superará al país A en el año {year} con una población " + str( poblacionB ) + " Vs. una población de " + str( poblacionA ) + " del país A.") 
# Imprime el año en que la población de B supera a la de A