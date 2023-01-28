import random


class ataque(object):
    def __init__(self, name, type, damage, accuracy, category):
        self.name = name
        self.type = type
        self.damage = damage
        self.accuracy = accuracy
        self.category = category

# Lista de movimientos con sus características
moves = [{"name": "Pound", "type": "Normal", "damage":40 , "accuracy": 1, "category": "Fisico"},
         {"name": "Karate Chop", "type": "Fight", "damage": 50, "accuracy": 1, "category": "Fisico"},
         {"name": "Doubleslap", "type": "Normal", "damage": 15, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Comet Punch", "type": "Normal", "damage": 18, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Mega Punch", "type": "Normal", "damage":80 , "accuracy": 1, "category": "Fisico"},
         {"name": "Pay Day", "type": "Normal", "damage": 40, "accuracy": 1, "category": "Fisico"},
         {"name": "Fire Punch", "type": "Fire", "damage": 75, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Ice Punch", "type": "Ice", "damage": 75, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Thunderpunch", "type": "Elect", "damage":75 , "accuracy": 1, "category": "Fisico"},
         {"name": "Scratch", "type": "Normal", "damage": 40, "accuracy": 1, "category": "Fisico"},
         {"name": "Vicegrip", "type": "Normal", "damage": 55, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Razor Wind", "type": "Normal", "damage":80 , "accuracy": 1, "category": "Fisico"},
         {"name": "Cut", "type": "Normal", "damage": 50, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Gust", "type": "Flying", "damage": 40, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Wing Attack", "type": "Flying", "damage":60 , "accuracy": 1, "category": "Fisico"},
         {"name": "Fly", "type": "Flying", "damage": 90, "accuracy": 1, "category": "Fisico"},
         {"name": "Bind", "type": "Normal", "damage": 15, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Slam", "type": "Normal", "damage": 80, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Vine Whip", "type": "Grass", "damage":35 , "accuracy": 1, "category": "Fisico"},
         {"name": "Stomp", "type": "Normal", "damage": 65, "accuracy": 1, "category": "Fisico"},
         {"name": "Double Kick", "type": "Fight", "damage": 30, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Mega Kick", "type": "Normal", "damage": 120, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Jump Kick", "type": "Fight", "damage":85, "accuracy": 1, "category": "Fisico"},
         {"name": "Rolling Kick", "type": "Fight", "damage": 60, "accuracy": 1, "category": "Fisico"},
         {"name": "Headbutt", "type": "Normal", "damage": 70, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Horn Attack", "type": "Normal", "damage":65, "accuracy": 1, "category": "Fisico"},
         {"name": "Fury Attack", "type": "Normal", "damage": 15, "accuracy": 1, "category": "Fisico"},
         {"name": "Tackle", "type": "Normal", "damage": 35, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Body Slam", "type": "Normal", "damage":85 , "accuracy": 1, "category": "Fisico"},
         {"name": "Wrap", "type": "Normal", "damage": 15, "accuracy": 1, "category": "Fisico"},
         {"name": "Take Down", "type": "Normal", "damage": 90, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Thrash", "type": "Normal", "damage": 90, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Double-Edge", "type": "Normal", "damage":120 , "accuracy": 1, "category": "Fisico"},
         {"name": "Poison Sting", "type": "Poison", "damage":15, "accuracy": 1, "category": "Fisico"},
         {"name": "Twineedle", "type": "Bug", "damage": 25, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Pin Missile", "type": "Bug", "damage": 14, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Bite", "type": "Dark", "damage": 60, "accuracy": 1, "category": "Fisico"},
         {"name": "Sonicboom", "type": "Normal", "damage": 20, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Acid", "type": "Poison", "damage": 40, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Ember", "type": "Fire", "damage":40 , "accuracy": 1, "category": "Fisico"},
         {"name": "Flamethrower", "type": "Fire", "damage": 95, "accuracy": 1, "category": "Fisico"},
         {"name": "Water Gun", "type": "Water", "damage": 40, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Hydro Pump", "type": "Water", "damage": 120, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Surf", "type": "Water", "damage":95 , "accuracy": 1, "category": "Fisico"},
         {"name": "Ice Beam", "type": "Ice", "damage": 95, "accuracy": 1, "category": "Fisico"},
         {"name": "Blizzard", "type": "Ice", "damage": 120, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Psybeam", "type": "Psychc", "damage": 65, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Bubblebeam", "type": "Water", "damage":65 , "accuracy": 1, "category": "Fisico"},
         {"name": "Aurora Beam", "type": "Ice", "damage": 65, "accuracy": 1, "category": "Fisico"},
         {"name": "Hyper Beam", "type": "Normal", "damage": 150, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Peck", "type": "Flying", "damage": 35, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Drill Peck", "type": "Flying", "damage":80 , "accuracy": 1, "category": "Fisico"},
         {"name": "Submission", "type": "Fight", "damage": 80, "accuracy": 1, "category": "Fisico"},
         {"name": "Low Kick", "type": "Fight", "damage": 50, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Counter", "type": "Fight", "damage": 70, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Seismic Toss", "type": "Fight", "damage":80 , "accuracy": 1, "category": "Fisico"},
         {"name": "Strength", "type": "Normal", "damage": 80, "accuracy": 1, "category": "Fisico"},
         {"name": "Absorb", "type": "Grass", "damage": 20, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Mega Drain", "type": "Grass", "damage": 40, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Razor Leaf", "type": "Grass", "damage":55 , "accuracy": 1, "category": "Fisico"},
         {"name": "Solarbeam", "type": "Grass", "damage": 120, "accuracy": 1, "category": "Fisico"},
         {"name": "Petal Dance", "type": "Grass", "damage": 90, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Dragon Rage", "type": "Dragon", "damage": 40, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Fire Spin", "type": "Fire", "damage":15 , "accuracy": 1, "category": "Fisico"},
         {"name": "Thundershock", "type": "Electr", "damage": 40, "accuracy": 1, "category": "Fisico"},
         {"name": "Thunderbolt", "type": "Electr", "damage": 95, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Thunder", "type": "Electr", "damage": 120, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Rock Throw", "type": "Rock", "damage":50 , "accuracy": 1, "category": "Fisico"},
         {"name": "Earthquake", "type": "Ground", "damage": 100, "accuracy": 1, "category": "Fisico"},
         {"name": "Fissure", "type": "Ground", "damage": 150, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Dig", "type": "Ground", "damage": 60, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Confusion", "type": "Psychc", "damage": 50, "accuracy": 1, "category": "Fisico"},
         {"name": "Psychic", "type": "Psychc", "damage": 90, "accuracy": 1, "category": "Fisico"},
         {"name": "Quick Attack", "type": "Normal", "damage": 40, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Rage", "type": "Normal", "damage": 20, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Selfdestruct", "type": "Normal", "damage": 200, "accuracy": 1, "category": "Fisico"},
         {"name": "Egg Bomb", "type": "Normal", "damage": 100, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Lick", "type": "Ghost", "damage": 20, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Smog", "type": "Poison", "damage":20 , "accuracy": 1, "category": "Fisico"},
         {"name": "Sludge", "type": "Poison", "damage": 65, "accuracy": 1, "category": "Fisico"},
         {"name": "Bone Club", "type": "Ground", "damage": 65, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Fire Blast", "type": "Fire", "damage": 120, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Waterfall", "type": "Water", "damage":80 , "accuracy": 1, "category": "Fisico"},
         {"name": "Clamp", "type": "Water", "damage": 35, "accuracy": 1, "category": "Fisico"},
         {"name": "Swift", "type": "Normal", "damage": 60, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Skull Bash", "type": "Normal", "damage": 100, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Spike Cannon", "type": "Normal", "damage":20 , "accuracy": 1, "category": "Fisico"},
         {"name": "Constrict", "type": "Normal", "damage": 10, "accuracy": 1, "category": "Fisico"},
         {"name": "Hi Jump Kick", "type": "Fight", "damage": 100, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Dream Eater", "type": "Psychc", "damage": 100, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Barrage", "type": "Normal", "damage": 15, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Leech Life", "type": "Bug", "damage": 20, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Sky Attack", "type": "Flying", "damage": 140, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Bubble", "type": "Water", "damage": 20, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Dizzy Punch", "type": "Normal", "damage": 70, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Crabhammer", "type": "Water", "damage": 90, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Explosion", "type": "Normal", "damage": 250, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Fury Swipes", "type": "Normal", "damage": 18, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Bonemerang", "type": "Ground", "damage": 50, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Rock Slide", "type": "Rock", "damage": 75, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Hyper Fang", "type": "Normal", "damage": 80, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Tri Attack", "type": "Normal", "damage": 80, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Super Fang", "type": "Normal", "damage": 100, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Slash", "type": "Normal", "damage": 70, "accuracy": 0.85, "category": "Fisico"},
         {"name": "Struggle", "type": "Normal", "damage": 50, "accuracy": 0.85, "category": "Fisico"}
         ]

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