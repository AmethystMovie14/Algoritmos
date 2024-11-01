#genotipo real
import random

# Definir el objetivo
objetivo = 983556

# Parámetros del algoritmo genético
tamaño_población = 300
probabilidad_mutación = 0.1
generaciones = 1000

# Función de aptitud: calcula la diferencia absoluta entre el individuo y el objetivo
def calcular_aptitud(individuo):
    return abs(objetivo - individuo)

# Crear un individuo aleatorio (un número entero)
def crear_individuo():
    return random.randint(0, 99999999)

# Crear una población inicial
def crear_población(tamaño):
    return [crear_individuo() for _ in range(tamaño)]

# Seleccionar dos individuos (padres) usando la selección por torneo
def seleccionar_padres(población):
    padres = random.sample(población, 2)
    padre1 = min(padres, key=calcular_aptitud)
    padre2 = max(padres, key=calcular_aptitud)
    return padre1, padre2

# Realizar cruce (crossover) entre dos padres
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, 7)  # Asumiendo que los números tienen 8 dígitos
    divisor = 10 ** punto_cruce
    hijo = (padre1 // divisor) * divisor + (padre2 % divisor)
    return hijo

# Aplicar mutación a un individuo
def mutar(individuo):
    individuo_str = list(str(individuo).zfill(8))  # Convertir a lista de caracteres con ceros iniciales si es necesario
    if random.random() < probabilidad_mutación:
        # Elegir un dígito aleatorio para mutar
        indice_mutacion = random.randint(0, 7)
        nuevo_valor = str(random.randint(0, 9))
        individuo_str[indice_mutacion] = nuevo_valor
    # Reconstruir el número a partir de la lista mutada
    return int(''.join(individuo_str))

# Algoritmo genético
def algoritmo_genetico():
    población = crear_población(tamaño_población)

    for generación in range(generaciones):
        población = sorted(población, key=calcular_aptitud)

        # Si el mejor individuo coincide con el objetivo, terminar
        mejor_individuo = población[0]
        mejor_aptitud = calcular_aptitud(mejor_individuo)
        print(f"Generación {generación}: Mejor individuo: {mejor_individuo} Aptitud: {mejor_aptitud}")

        if mejor_individuo == objetivo:
            print("¡Objetivo alcanzado!")
            break

        nueva_población = población[:2]  # Mantener los mejores dos individuos (elitismo)

        while len(nueva_población) < tamaño_población:
            padre1, padre2 = seleccionar_padres(población)
            hijo = cruzar(padre1, padre2)
            hijo_mutado = mutar(hijo)
            nueva_población.append(hijo_mutado)

        población = nueva_población

    return mejor_individuo

# Ejecutar el algoritmo genético
solución = algoritmo_genetico()
print(f"Solución encontrada: {solución}")
