import random

#ALGORITMO GENETICO UTILIZADO EN EL SCRIPT PROYECTOPOKEMON.py

class ataque(object):
    def __init__(self, name, type, damage, accuracy, category):
        self.name = name
        self.type = type
        self.damage = damage
        self.accuracy = accuracy
        self.category = category

# Lista de movimientos con sus características

# Función de fitness: calcula el poder de ataque de cada movimiento
#def fitness(move):
#    score = move["damage"] * move["accuracy"]
#    if move["category"] == "Físico":
#        score += 10
#    return score
#
## Función para crear una población inicial
#def create_population(size):
#    population = []
#    for i in range(size):
#        population.append(random.choice(moves))
#    return population
#
## Función para seleccionar individuos para reproducirse
#def select_individuals(population):
#    individuals = []
#    for i in range(len(population)):
#        if fitness(population[i]) > random.randint(0, 100):
#            individuals.append(population[i])
#    return individuals
#
## Función para reproducirse
#def reproduce(individuals):
#    offspring = []
#    while len(individuals) > 0:
#        parent1 = individuals.pop(random.randint(0, len(individuals) - 1))
#        parent2 = individuals.pop(random.randint(0, len(individuals) - 1))
#        offspring.append(parent1)
#        offspring.append(parent2)
#    return offspring
#
## Función para mutar
#def mutate(population):
#    for i in range(len(population)):
#        if random.randint(0, 100) < 5:
#            population[i] = random.choice(moves)
#
## Algoritmo genético
#population = create_population(100)
#for i in range(1000):
#    individuals = select_individuals(population)
#    population = reproduce(individuals)
#    mutate(population)
#
## Encuentra el mejor movimiento
#best_move = max(population, key=fitness)
#print("El mejor movimiento es: " + best_move["name"])
#