import numpy as np

class Particle:
    def __init__(self, bounds):
        self.position = np.random.uniform(bounds[0], bounds[1])
        self.velocity = np.random.uniform(-1, 1)
        self.best_position = self.position
        self.best_value = float('inf')

    def evaluate(self, fitness_function):
        value = fitness_function(self.position)
        if value < self.best_value:
            self.best_value = value
            self.best_position = self.position

    def update(self, global_best_position, w, c1, c2):
        r1, r2 = np.random.rand(2)
        self.velocity = (w * self.velocity +
                         c1 * r1 * (self.best_position - self.position) +
                         c2 * r2 * (global_best_position - self.position))
        self.position += self.velocity


def fitness_function(x):
    return x**2  


def pso(num_particles, bounds, num_iterations, w, c1, c2):
    particles = [Particle(bounds) for _ in range(num_particles)]
    global_best_position = float('inf')
    global_best_value = float('inf')

    for _ in range(num_iterations):
        for particle in particles:
            particle.evaluate(fitness_function)
            if particle.best_value < global_best_value:
                global_best_value = particle.best_value
                global_best_position = particle.best_position

        for particle in particles:
            particle.update(global_best_position, w, c1, c2)

    return global_best_position, global_best_value

num_particles = 30
bounds = (-10, 10)
num_iterations = 100
w = 0.5      
c1 = 1.5    
c2 = 1.5    

best_position, best_value = pso(num_particles, bounds, num_iterations, w, c1, c2)

print("Mejor posición:", best_position)
print("Mejor valor:", best_value)
