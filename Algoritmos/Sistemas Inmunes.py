import random

def fitness(solution):
    return sum(solution)  
def initialize_population(size, dimensions):
    return [random.sample(range(0, 10), dimensions) for _ in range(size)]

def select_best(population, fitness_scores, n):
    sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
    return [sol for sol, _ in sorted_population[:n]]

def mutate(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.randint(0, 10)
    return solution

def immune_algorithm(iterations, population_size, dimensions, mutation_rate):
    population = initialize_population(population_size, dimensions)

    for _ in range(iterations):
        fitness_scores = [fitness(sol) for sol in population]

        best_solutions = select_best(population, fitness_scores, population_size // 2)

        new_population = best_solutions[:]
        
        for sol in best_solutions:
            if random.random() < mutation_rate:
                new_solution = mutate(sol.copy())
                new_population.append(new_solution)

        population = new_population

    final_fitness_scores = [fitness(sol) for sol in population]
    best_solution = max(population, key=fitness)
    
    return best_solution, fitness(best_solution)

iterations = 100
population_size = 20
dimensions = 5
mutation_rate = 0.1

best_solution, best_fitness = immune_algorithm(iterations, population_size, dimensions, mutation_rate)
print("Mejor solución:", best_solution)
print("Mejor fitness:", best_fitness)
