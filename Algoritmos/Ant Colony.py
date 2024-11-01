print("Ant Colony")
print ("MY CODE IS ")
import numpy as np

# Configuración inicial
NUM_CIUDADES = 5
NUM_HORMIGAS = 10
NUM_ITERACIONES = 100
ALFA = 1.0  # Influencia de la feromona
BETA = 5.0  # Influencia de la distancia
RHO = 0.5   # Evaporación de feromona
Q = 100     # Constante para depósito de feromonas

# Generar un grafo de distancias (simétrico)
np.random.seed(84)
distancias = np.random.randint(1, 100, size=(NUM_CIUDADES, NUM_CIUDADES))
np.fill_diagonal(distancias, 0)
distancias = (distancias + distancias.T) / 2  # Matriz simétrica

# Inicializar la matriz de feromonas
feromonas = np.ones((NUM_CIUDADES, NUM_CIUDADES))

# Función de probabilidad de elección de la siguiente ciudad
def seleccionar_siguiente_ciudad(feromonas, distancias, ciudad_actual, ciudades_no_visitadas):
    probabilidades = []
    for ciudad in ciudades_no_visitadas:
        # Regla de transición de la hormiga
        tau = feromonas[ciudad_actual][ciudad] ** ALFA
        eta = (1.0 / distancias[ciudad_actual][ciudad]) ** BETA
        probabilidades.append(tau * eta)

    probabilidades = np.array(probabilidades)
    probabilidades /= probabilidades.sum()  # Normalizar

    # Seleccionar la siguiente ciudad
    siguiente_ciudad = np.random.choice(ciudades_no_visitadas, p=probabilidades)
    return siguiente_ciudad

# Simular el recorrido de las hormigas
def recorrido_hormiga(feromonas, distancias):
    recorrido = []
    ciudades_no_visitadas = list(range(NUM_CIUDADES))
    ciudad_actual = np.random.choice(ciudades_no_visitadas)
    recorrido.append(ciudad_actual)
    ciudades_no_visitadas.remove(ciudad_actual)

    while ciudades_no_visitadas:
        siguiente_ciudad = seleccionar_siguiente_ciudad(feromonas, distancias, ciudad_actual, ciudades_no_visitadas)
        recorrido.append(siguiente_ciudad)
        ciudades_no_visitadas.remove(siguiente_ciudad)
        ciudad_actual = siguiente_ciudad

    return recorrido

# Función para calcular la longitud del recorrido
def calcular_longitud_recorrido(recorrido, distancias):
    longitud = 0
    for i in range(len(recorrido) - 1):
        longitud += distancias[recorrido[i]][recorrido[i+1]]
    # Volver al punto de inicio
    longitud += distancias[recorrido[-1]][recorrido[0]]
    return longitud

# Actualizar la feromona
def actualizar_feromonas(feromonas, hormigas_recorridos, hormigas_longitudes):
    # Evaporación de feromonas
    feromonas *= (1 - RHO)

    # Añadir nuevas feromonas basadas en el recorrido
    for i, recorrido in enumerate(hormigas_recorridos):
        delta_feromona = Q / hormigas_longitudes[i]
        for j in range(len(recorrido) - 1):
            feromonas[recorrido[j]][recorrido[j+1]] += delta_feromona
            feromonas[recorrido[j+1]][recorrido[j]] += delta_feromona

# Algoritmo principal
def colonia_de_hormigas():
    mejor_recorrido = None
    mejor_longitud = float('inf')

    for iteracion in range(NUM_ITERACIONES):
        hormigas_recorridos = []
        hormigas_longitudes = []

        # Las hormigas recorren el grafo
        for _ in range(NUM_HORMIGAS):
            recorrido = recorrido_hormiga(feromonas, distancias)
            longitud = calcular_longitud_recorrido(recorrido, distancias)

            hormigas_recorridos.append(recorrido)
            hormigas_longitudes.append(longitud)

            if longitud < mejor_longitud:
                mejor_recorrido = recorrido
                mejor_longitud = longitud

        # Actualizar feromonas basado en los recorridos de las hormigas
        actualizar_feromonas(feromonas, hormigas_recorridos, hormigas_longitudes)

        print(f"Iteración {iteracion + 1}, mejor longitud: {mejor_longitud}")

    return mejor_recorrido, mejor_longitud

# Ejecutar el algoritmo
mejor_recorrido, mejor_longitud = colonia_de_hormigas()
print("\nMejor recorrido encontrado:", mejor_recorrido)
print("Longitud del mejor recorrido:", mejor_longitud)