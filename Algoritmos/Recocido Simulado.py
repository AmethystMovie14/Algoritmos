import numpy as np
import math
import random

def calcular_distancia(ruta, distancias):
    distancia = 0
    for i in range(len(ruta)):
        distancia += distancias[ruta[i], ruta[(i + 1) % len(ruta)]]
    return distancia

def generar_vecino(ruta):
    nueva_ruta = ruta.copy()
    i, j = random.sample(range(len(ruta)), 2)
    nueva_ruta[i], nueva_ruta[j] = nueva_ruta[j], nueva_ruta[i]
    return nueva_ruta

def recocido_simulado(distancias, temperatura_inicial=1000, tasa_enfriamiento=0.995, iteraciones=1000):
    num_ciudades = len(distancias)
    # Solución inicial: una ruta aleatoria
    ruta_actual = list(range(num_ciudades))
    random.shuffle(ruta_actual)
    mejor_ruta = ruta_actual.copy()
    mejor_distancia = calcular_distancia(mejor_ruta, distancias)
    
    T = temperatura_inicial
    
    for _ in range(iteraciones):
        ruta_vecina = generar_vecino(ruta_actual)
        distancia_actual = calcular_distancia(ruta_actual, distancias)
        distancia_vecina = calcular_distancia(ruta_vecina, distancias)
        delta_E = distancia_vecina - distancia_actual
        
        if delta_E < 0 or random.random() < math.exp(-delta_E / T):
            ruta_actual = ruta_vecina
            if distancia_vecina < mejor_distancia:
                mejor_ruta = ruta_vecina
                mejor_distancia = distancia_vecina
        
        T *= tasa_enfriamiento  # Actualizar temperatura
    
    return mejor_ruta, mejor_distancia

# Ejemplo de uso:
if __name__ == "__main__":
    # Matriz de distancias entre 5 ciudades
    distancias = np.array([
        [0, 2, 9, 10, 7],
        [1, 0, 6, 4, 3],
        [15, 7, 0, 8, 3],
        [6, 3, 12, 0, 11],
        [10, 4, 8, 5, 0]
    ])
    
    mejor_ruta, mejor_distancia = recocido_simulado(distancias, temperatura_inicial=1000, tasa_enfriamiento=0.995, iteraciones=10000)
    print("Mejor ruta encontrada:", mejor_ruta)
    print("Distancia de la mejor ruta:", mejor_distancia)
