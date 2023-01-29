import random

# Lista de movimientos con sus características
moves = [{"name": "Pound", "type": "Normal", "damage": 40, "accuracy": 1, "category": "Fisico"},
         {"name": "Karate Chop", "type": "Fight", "damage": 50,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Doubleslap", "type": "Normal", "damage": 15,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Comet Punch", "type": "Normal", "damage": 18,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Mega Punch", "type": "Normal", "damage": 80,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Pay Day", "type": "Normal", "damage": 40,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Fire Punch", "type": "Fire", "damage": 75,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Ice Punch", "type": "Ice", "damage": 75,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Thunderpunch", "type": "Elect",
             "damage": 75, "accuracy": 1, "category": "Fisico"},
         {"name": "Scratch", "type": "Normal", "damage": 40,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Vicegrip", "type": "Normal", "damage": 55,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Razor Wind", "type": "Normal", "damage": 80,
             "accuracy": 1, "category": "Especial"},
         {"name": "Cut", "type": "Normal", "damage": 50,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Gust", "type": "Flying", "damage": 40,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Wing Attack", "type": "Flying",
             "damage": 60, "accuracy": 1, "category": "Fisico"},
         {"name": "Fly", "type": "Flying", "damage": 90,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Bind", "type": "Normal", "damage": 15,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Slam", "type": "Normal", "damage": 80,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Vine Whip", "type": "Grass", "damage": 35,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Stomp", "type": "Normal", "damage": 65,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Double Kick", "type": "Fight", "damage": 30,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Mega Kick", "type": "Normal", "damage": 120,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Jump Kick", "type": "Fight", "damage": 85,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Rolling Kick", "type": "Fight",
             "damage": 60, "accuracy": 1, "category": "Fisico"},
         {"name": "Headbutt", "type": "Normal", "damage": 70,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Horn Attack", "type": "Normal",
             "damage": 65, "accuracy": 1, "category": "Fisico"},
         {"name": "Fury Attack", "type": "Normal",
             "damage": 15, "accuracy": 1, "category": "Fisico"},
         {"name": "Tackle", "type": "Normal", "damage": 35,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Body Slam", "type": "Normal", "damage": 85,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Wrap", "type": "Normal", "damage": 15,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Take Down", "type": "Normal", "damage": 90,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Thrash", "type": "Normal", "damage": 90,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Double-Edge", "type": "Normal",
             "damage": 120, "accuracy": 1, "category": "Fisico"},
         {"name": "Poison Sting", "type": "Poison",
             "damage": 15, "accuracy": 1, "category": "Fisico"},
         {"name": "Twineedle", "type": "Bug", "damage": 25,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Pin Missile", "type": "Bug", "damage": 14,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Bite", "type": "Dark", "damage": 60,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Sonicboom", "type": "Normal", "damage": 20,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Acid", "type": "Poison", "damage": 40,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Ember", "type": "Fire", "damage": 40,
             "accuracy": 1, "category": "Especial"},
         {"name": "Flamethrower", "type": "Fire", "damage": 95,
             "accuracy": 1, "category": "Especial"},
         {"name": "Water Gun", "type": "Water", "damage": 40,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Hydro Pump", "type": "Water", "damage": 120,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Surf", "type": "Water", "damage": 95,
             "accuracy": 1, "category": "Especial"},
         {"name": "Ice Beam", "type": "Ice", "damage": 95,
             "accuracy": 1, "category": "Especial"},
         {"name": "Blizzard", "type": "Ice", "damage": 120,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Psybeam", "type": "Psychc", "damage": 65,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Bubblebeam", "type": "Water", "damage": 65,
             "accuracy": 1, "category": "Especial"},
         {"name": "Aurora Beam", "type": "Ice", "damage": 65,
             "accuracy": 1, "category": "Especial"},
         {"name": "Hyper Beam", "type": "Normal", "damage": 150,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Peck", "type": "Flying", "damage": 35,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Drill Peck", "type": "Flying", "damage": 80,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Submission", "type": "Fight", "damage": 80,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Low Kick", "type": "Fight", "damage": 50,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Counter", "type": "Fight", "damage": 70,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Seismic Toss", "type": "Fight",
             "damage": 80, "accuracy": 1, "category": "Fisico"},
         {"name": "Strength", "type": "Normal", "damage": 80,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Absorb", "type": "Grass", "damage": 20,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Mega Drain", "type": "Grass", "damage": 40,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Razor Leaf", "type": "Grass", "damage": 55,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Solarbeam", "type": "Grass", "damage": 120,
             "accuracy": 1, "category": "Especial"},
         {"name": "Petal Dance", "type": "Grass", "damage": 90,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Dragon Rage", "type": "Dragon", "damage": 40,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Fire Spin", "type": "Fire", "damage": 15,
             "accuracy": 1, "category": "Especial"},
         {"name": "Thundershock", "type": "Electr", "damage": 40,
             "accuracy": 1, "category": "Especial"},
         {"name": "Thunderbolt", "type": "Electr", "damage": 95,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Thunder", "type": "Electr", "damage": 120,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Rock Throw", "type": "Rock", "damage": 50,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Earthquake", "type": "Ground", "damage": 100,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Fissure", "type": "Ground", "damage": 150,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Dig", "type": "Ground", "damage": 60,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Confusion", "type": "Psychc", "damage": 50,
             "accuracy": 1, "category": "Especial"},
         {"name": "Psychic", "type": "Psychc", "damage": 90,
             "accuracy": 1, "category": "Especial"},
         {"name": "Quick Attack", "type": "Normal", "damage": 40,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Rage", "type": "Normal", "damage": 20,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Selfdestruct", "type": "Normal",
             "damage": 200, "accuracy": 1, "category": "Fisico"},
         {"name": "Egg Bomb", "type": "Normal", "damage": 100,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Lick", "type": "Ghost", "damage": 20,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Smog", "type": "Poison", "damage": 20,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Sludge", "type": "Poison", "damage": 65,
             "accuracy": 1, "category": "Especial"},
         {"name": "Bone Club", "type": "Ground", "damage": 65,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Fire Blast", "type": "Fire", "damage": 120,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Waterfall", "type": "Water", "damage": 80,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Clamp", "type": "Water", "damage": 35,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Swift", "type": "Normal", "damage": 60,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Skull Bash", "type": "Normal", "damage": 100,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Spike Cannon", "type": "Normal",
             "damage": 20, "accuracy": 1, "category": "Fisico"},
         {"name": "Constrict", "type": "Normal", "damage": 10,
             "accuracy": 1, "category": "Fisico"},
         {"name": "Hi Jump Kick", "type": "Fight", "damage": 100,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Dream Eater", "type": "Psychc", "damage": 100,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Barrage", "type": "Normal", "damage": 15,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Leech Life", "type": "Bug", "damage": 20,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Sky Attack", "type": "Flying", "damage": 140,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Bubble", "type": "Water", "damage": 20,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Dizzy Punch", "type": "Normal", "damage": 70,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Crabhammer", "type": "Water", "damage": 90,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Explosion", "type": "Normal", "damage": 250,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Fury Swipes", "type": "Normal", "damage": 18,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Bonemerang", "type": "Ground", "damage": 50,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Rock Slide", "type": "Rock", "damage": 75,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Hyper Fang", "type": "Normal", "damage": 80,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Tri Attack", "type": "Normal", "damage": 80,
             "accuracy": 0.85, "category": "Especial"},
         {"name": "Super Fang", "type": "Normal", "damage": 100,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Slash", "type": "Normal", "damage": 70,
             "accuracy": 0.85, "category": "Fisico"},
         {"name": "Struggle", "type": "Normal", "damage": 50,
             "accuracy": 0.85, "category": "Fisico"}
         ]

efectividad = [{"tipo": "Water", "tipoRival": "Water", "valor": 0.5},
               {"tipo": "Water", "tipoRival": "Dragon", "valor": 0.5},
               {"tipo": "Water", "tipoRival": "Fire", "valor": 2},
               {"tipo": "Water", "tipoRival": "Grass", "valor": 0.5},
               {"tipo": "Water", "tipoRival": "Rock", "valor": 2},
               {"tipo": "Water", "tipoRival": "Ground", "valor": 2},
               {"tipo": "Bug", "tipoRival": "Fire", "valor": 0.5},
               {"tipo": "Bug", "tipoRival": "Fight", "valor": 0.5},
               {"tipo": "Bug", "tipoRival": "Grass", "valor": 2},
               {"tipo": "Bug", "tipoRival": "Psychc", "valor": 2},
               {"tipo": "Bug", "tipoRival": "Poison", "valor": 2},
               {"tipo": "Bug", "tipoRival": "Flying", "valor": 0.5},
               {"tipo": "Dragon", "tipoRival": "Dragon", "valor": 2},
               {"tipo": "Elect", "tipoRival": "Water", "valor": 2},
               {"tipo": "Elect", "tipoRival": "Dragon", "valor": 0.5},
               {"tipo": "Elect", "tipoRival": "Elect", "valor": 0.5},
               {"tipo": "Elect", "tipoRival": "Grass", "valor": 0.5},
               {"tipo": "Elect", "tipoRival": "Ground", "valor": 0},
               {"tipo": "Elect", "tipoRival": "Flying", "valor": 2},
               {"tipo": "Ghost", "tipoRival": "Ghost", "valor": 2},
               {"tipo": "Ghost", "tipoRival": "Normal", "valor": 0},
               {"tipo": "Ghost", "tipoRival": "Psychc", "valor": 0},
               {"tipo": "Fire", "tipoRival": "Water", "valor": 0.5},
               {"tipo": "Fire", "tipoRival": "Bug", "valor": 2},
               {"tipo": "Fire", "tipoRival": "Dragon", "valor": 0.5},
               {"tipo": "Fire", "tipoRival": "Fire", "valor": 0.5},
               {"tipo": "Fire", "tipoRival": "Ice", "valor": 2},
               {"tipo": "Fire", "tipoRival": "Grass", "valor": 2},
               {"tipo": "Fire", "tipoRival": "Rock", "valor": 0.5},
               {"tipo": "Ice", "tipoRival": "Water", "valor": 0.5},
               {"tipo": "Ice", "tipoRival": "Dragon", "valor": 2},
               {"tipo": "Ice", "tipoRival": "Ice", "valor": 0.5},
               {"tipo": "Ice", "tipoRival": "Grass", "valor": 2},
               {"tipo": "Ice", "tipoRival": "Ground", "valor": 2},
               {"tipo": "Ice", "tipoRival": "Flying", "valor": 2},
               {"tipo": "Fight", "tipoRival": "Bug", "valor": 0.5},
               {"tipo": "Fight", "tipoRival": "Ghost", "valor": 0},
               {"tipo": "Fight", "tipoRival": "Ice", "valor": 2},
               {"tipo": "Fight", "tipoRival": "Normal", "valor": 2},
               {"tipo": "Fight", "tipoRival": "Psychc", "valor": 0.5},
               {"tipo": "Fight", "tipoRival": "Rock", "valor": 2},
               {"tipo": "Fight", "tipoRival": "Poison", "valor": 0.5},
               {"tipo": "Fight", "tipoRival": "Flying", "valor": 0.5},
               {"tipo": "Normal", "tipoRival": "Ghost", "valor": 0},
               {"tipo": "Normal", "tipoRival": "Rock", "valor": 0.5},
               {"tipo": "Grass", "tipoRival": "Water", "valor": 2},
               {"tipo": "Grass", "tipoRival": "Bug", "valor": 0.5},
               {"tipo": "Grass", "tipoRival": "Dragon", "valor": 0.5},
               {"tipo": "Grass", "tipoRival": "Fire", "valor": 0.5},
               {"tipo": "Grass", "tipoRival": "Grass", "valor": 0.5},
               {"tipo": "Grass", "tipoRival": "Rock", "valor": 2},
               {"tipo": "Grass", "tipoRival": "Ground", "valor": 2},
               {"tipo": "Grass", "tipoRival": "Poison", "valor": 0.5},
               {"tipo": "Grass", "tipoRival": "Flying", "valor": 0.5},
               {"tipo": "Psychc", "tipoRival": "Fight", "valor": 2},
               {"tipo": "Psychc", "tipoRival": "Psychc", "valor": 0.5},
               {"tipo": "Psychc", "tipoRival": "Poison", "valor": 2},
               {"tipo": "Rock", "tipoRival": "Bug", "valor": 2},
               {"tipo": "Rock", "tipoRival": "Fire", "valor": 2},
               {"tipo": "Rock", "tipoRival": "Ice", "valor": 2},
               {"tipo": "Rock", "tipoRival": "Fight", "valor": 0.5},
               {"tipo": "Rock", "tipoRival": "Ground", "valor": 0.5},
               {"tipo": "Rock", "tipoRival": "Flying", "valor": 2},
               {"tipo": "Ground", "tipoRival": "Bug", "valor": 0.5},
               {"tipo": "Ground", "tipoRival": "Elect", "valor": 2},
               {"tipo": "Ground", "tipoRival": "Fire", "valor": 2},
               {"tipo": "Ground", "tipoRival": "Grass", "valor": 0.5},
               {"tipo": "Ground", "tipoRival": "Rock", "valor": 2},
               {"tipo": "Ground", "tipoRival": "Poison", "valor": 2},
               {"tipo": "Ground", "tipoRival": "Flying", "valor": 0},
               {"tipo": "Poison", "tipoRival": "Bug", "valor": 2},
               {"tipo": "Poison", "tipoRival": "Ghost", "valor": 0.5},
               {"tipo": "Poison", "tipoRival": "Grass", "valor": 2},
               {"tipo": "Poison", "tipoRival": "Rock", "valor": 0.5},
               {"tipo": "Poison", "tipoRival": "Ground", "valor": 0.5},
               {"tipo": "Poison", "tipoRival": "Poison", "valor": 0.5},
               {"tipo": "Flying", "tipoRival": "Bug", "valor": 2},
               {"tipo": "Flying", "tipoRival": "Elect", "valor": 0.5},
               {"tipo": "Flying", "tipoRival": "Fight", "valor": 2},
               {"tipo": "Flying", "tipoRival": "Grass", "valor": 2},
               {"tipo": "Flying", "tipoRival": "Rock", "valor": 0.5}
               ]

# Función para formula de daño


def damage_function(bonificacion, nivel, ataque, poder):
    i = random.randint(96, 419)
    return 0.01 * bonificacion * (((0.2 * nivel + 1) * ataque * poder) / (25 * i) + 2)

# Función de busqueda por tipos de valor de efectividad


def get_efectividad_data(tipo, tipoRival, efectividad):
    valorEfectividad = 1
    for item in efectividad:
        if item["tipo"] == tipo and item["tipoRival"] == tipoRival[0]:
            valorEfectividad *= item["valor"]
    for item in efectividad:
        if item["tipo"] == tipo and item["tipoRival"] == tipoRival[1]:
            valorEfectividad *= item["valor"]
    return valorEfectividad

# Funcion de busqueda por nombre en moves


def get_move_data(name, moves):
    for move in moves:
        if move["name"] == name:
            return move
    return None

# Función de fitness: calcula el poder de ataque de cada movimiento


def fitness(move, ataque, ataqueEspecial, tipoRival):
    if move["category"] == "Fisico":
        score = damage_function(get_efectividad_data(
            move["type"], tipoRival, efectividad), 80, ataque, move["damage"]) * move["accuracy"]
    else:
        score = damage_function(get_efectividad_data(
            move["type"], tipoRival, efectividad), 80, ataqueEspecial, move["damage"]) * move["accuracy"]
    return score

# Encuentra el mejor movimiento


def best_move(move1, move2, move3, move4, ataque, ataqueEspecial, tipoRival):
    f1 = fitness(move1, ataque, ataqueEspecial, tipoRival)
    f2 = fitness(move2, ataque, ataqueEspecial, tipoRival)
    f3 = fitness(move3, ataque, ataqueEspecial, tipoRival)
    f4 = fitness(move4, ataque, ataqueEspecial, tipoRival)
    mejor = max(f1, f2, f3, f4)
    if mejor > 0.5:
        if mejor == f1:
            return 0
        if mejor == f2:
            return 1
        if mejor == f3:
            return 2
        if mejor == f4:
            return 3
    else:
        return 5


print(best_move(get_move_data("Explosion", moves), get_move_data("Surf", moves),
      get_move_data("Peck", moves), get_move_data("Lick", moves), 90, 120, ["Fire", ""]))
