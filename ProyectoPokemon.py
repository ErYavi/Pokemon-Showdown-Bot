import numpy as np
import cv2
from PIL import ImageOps, Image
import pyautogui as py
import time
import win32gui as wg
import win32api
from pytesseract import *
from Objetos import *
import copy
import tipos
import eleccionMovimiento as el
import random

# Lista de movimientos con sus caracterÃ­sticas
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

#tablas de efectividad
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

# Funcion para formula de dato
def damage_function(bonificacion, nivel, ataque, poder):
    i = random.randint(96, 419)
    return 0.01 * bonificacion * (((0.2 * nivel + 1) * ataque * poder) / (25 * i) + 2)

# Funcion de busqueda por tipos de valor de efectividad
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

# Funcion de fitness: calcula el poder de ataque de cada movimiento
def fitness(move, ataque, ataqueEspecial, tipoRival):
    if tipoRival == ["", ""]:
        tipoRival = ["Normal", ""]
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

################################################################
#   SELECCIONAR AREA DE PANTALLA
xa, ya, xb, yb = 0, 0, 0, 0
switch = False
option = ""

def dibujar(event, x, y, flags, param):
    global xa, ya, xb, yb, switch
    if event == cv2.EVENT_LBUTTONDOWN:
        xa, ya = x, y
        switch = False
    if event == cv2.EVENT_LBUTTONUP:
        xb, yb = x, y
        switch = True

def aceptar(title='', text='', button='OK'):
    py.alert(title=title, text=text, button=button)
    win32handles = py.getWindowsWithTitle(title)
    if win32handles:
        wg.SetForegroundWindow(win32handles[0])

pantalla = cv2.cvtColor(np.array(py.screenshot()), cv2.COLOR_BGR2RGB)

cv2.namedWindow("screen", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback("screen", dibujar)

while option != "yes":
    img = copy.copy(pantalla)
    if switch == True:
        cv2.rectangle(img, (xa, ya), (xb, yb), (0, 0, 200), 1)
        cv2.imshow("screen", img)
        option = py.confirm(
            "Game area correctly selected?\nIt must include all the game screen plus your attacks and pokémon, but must NOT include any fo the browser borders or the PokemonShowDown banner. Otherwise the bot will not work\nDO NOT MOVE THE MOUSE AFTER PRESSING YES", "Confirm", ["yes", "no"])
        if option != "yes":
            switch = False
            aceptar(title="SELECT GAME AREA",
                    text="Select the game area, then press [Accept]")
    cv2.imshow("screen", img)
    if option != "yes" and switch != True:
        aceptar(title="SELECT GAME AREA",
                text="Select the game area, then press [Accept]")
    cv2.waitKey(1)
cv2.destroyAllWindows()
time.sleep(1)
#print("sin ordenar:\n("+str(xa)+", "+str(ya)+")("+str(xb)+", "+str(yb)+")")

# Ordena las coordenadas para que xa e ya sean la esquina superior izquierda del juego
if xa > xb:
    aux = copy.copy(xa)
    xa = copy.copy(xb)
    xb = copy.copy(aux)
if ya > yb:
    aux = copy.copy(ya)
    ya = copy.copy(yb)
    yb = copy.copy(aux)

#print("ordenadas:\n("+str(xa)+", "+str(ya)+")("+str(xb)+", "+str(yb)+")")
#################################################################################

#   FUNCIONES

def encontrarDato(s, texto):
    if s != 'HP':
        i = texto.rfind('Atk')
        if s == 'Def':
            i += 10
        elif s == 'Spc':
            i += 20
        elif s == 'Spe':
            i += 30
    else:
        i = texto.rfind(s)
    j = 4
    dato = ""
    while ("0" <= texto[i+j] <= "9") or texto[i+j] == "." or texto[i+1] == None:
        dato += texto[i+j]
        j += 1
    return dato

def leerTipo(img):
    type = 0
    i = 0
    umbral = 0.6
    datos = []
    while type < 2 and i < len(tipos.nombres):
        # Va leyendo todas las templates y ajusta su tamaño
        template = cv2.imread(tipos.templates[i])
        template = cv2.resize(template, (0, 0), fx=31/255, fy=11/95)
        # Buscar plantilla en imagen
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        # Encuentra la mejor coincidencia
        _, max_val, _, _ = cv2.minMaxLoc(res)
        # Comprobamos que la coincidencia sea mayor a 0,6 (que es el umbral de funcionamiento)
        if max_val > umbral:
            type += 1
            datos.append(tipos.nombres[i])
        i += 1
    if len(datos) < 2:
        while len(datos) < 2:
            datos.append("")
    return datos

def leerAtaques():
    imagen = py.screenshot(region=(0+xa, 417+ya, 637, 21))
    imagen = py.screenshot(region=(0+0, 417+128, 637, 21))
    ataques = []
    for i in range(0, 4):
        img = imagen.crop((155*i + 10,  0,  155*i + 150, 20))
        ataque = pytesseract.image_to_string(img, lang="eng")
        ataques.append(ataque)
    #print(ataques)

    return ataques

def leerPokemon(x, y):
    global pokemon
    # pone cursor en posicion
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    # screenshot
    screen = py.screenshot(region=(x-45, 338 + ya, 250, 138))
    # screen.show()
    # guardar datos
    texto = pytesseract.image_to_string(screen, lang='eng')
    print(texto)
    vida = encontrarDato("HP", texto)
    # print(vida)
    ataque = encontrarDato("Atk", texto)
    # print(ataque)
    defensa = encontrarDato("Def", texto)
    # print(defensa)
    especial = encontrarDato("Spc", texto)
    # print(especial)
    velocidad = encontrarDato("Spe", texto)
    # print(velocidad)
    types = leerTipo(np.array(screen))
    # crea objeto pokemon
    pokemonActual = Pokemon(types, vida, ataque, defensa, especial, velocidad, None)

    return pokemonActual

def LeerPokemonEnemigo():
    win32api.SetCursorPos((410 + xa, 123 + ya))
    time.sleep(0.2)
    screen2 = py.screenshot(region=(389+xa, 11+ya, 300, 75))
    # screen2.show()
    texto2 = pytesseract.image_to_string(screen2)
    print(texto2)
    types = leerTipo(np.array(screen2))
    enemigo = Pokemon(types, encontrarDato("HP", texto2), None, None, None, None, None)
    return enemigo

def cambiarPokemon(cambio):
    win32api.SetCursorPos((xPokemon[cambio], yPokemon))
    py.click()

def cambiarPokemonDebilitado(cambio):
    win32api.SetCursorPos((xPokemon[cambio], yPokemon-75))
    py.click()

def leerBanquillo(pokemon):
    for i in range(1, 6):
        aux = leerPokemon(xPokemon[i], yPokemon)
        pokemon = np.append(pokemon, aux)
        print("Pokemon posicion ", i, ": ")
        pokemon[i].mostrar()

    return pokemon

def leerActual(x, y):
    global pokemon
    # pone cursor en posicion
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)
    # screenshot
    screen = py.screenshot(region=(xa + 125, 117 + ya, 300, 80))
    # screen.show()
    # guardar datos
    texto = pytesseract.image_to_string(screen, lang='eng')
    print(texto)
    vida = encontrarDato("HP", texto)
    # print(vida)
    ataque = encontrarDato("Atk", texto)
    # print(ataque)
    defensa = encontrarDato("Def", texto)
    # print(defensa)
    especial = encontrarDato("Spc", texto)
    # print(especial)
    velocidad = encontrarDato("Spe", texto)
    # print(velocidad)
    # crea objeto pokemon
    types = leerTipo(np.array(screen))

    pokemonActual = Pokemon(types, vida, ataque, defensa, especial, velocidad, leerAtaques())
    return pokemonActual

def seleccionarAtaque(posicion):
    win32api.SetCursorPos((xAtaques[posicion], yAtaques))
    py.click()

def leerTodo():
    global pokemon
    # lee pokemon actual
    pokemon = np.append(pokemon, (leerActual(x, y)))
    print("# POKEMON ACTUAL: #")
    pokemon[0].mostrar()
    # lee banquillo
    print("# POKEMONS EN EL BANQUILLO #")
    leerBanquillo(pokemon)
    # lee enemigo
    print("# POKEMON ENEMIGO #")
    global enemigo
    enemigo = LeerPokemonEnemigo()
    enemigo.mostrar()

def espera():
    wait = py.screenshot(region=(xa + 0, 400 + ya, 640, 140))
    texto0 = pytesseract.image_to_string(wait)
    if "Waiting for opponent..." in texto0:
        time.sleep(10)
        return False
    else:
        return True

def detectarDebilitado():
    screen = py.screenshot(region=(xa + 111, ya + 328, 128, 24))
    screen = ImageOps.invert(screen)
    #screen.show()
    texto = pytesseract.image_to_string(screen)
    #print(texto)
    i=1
    while "fainted" in texto:
        cambiarPokemonDebilitado(i)
        i+=1
    time.sleep(5)

#################################################################################
# Coordenada para tapar chat
xChat, yChat = 700 + xa, 16 + ya
win32api.SetCursorPos((xChat, yChat))
py.click()

# Coordenadas para leer datos pokemon
x, y = 200+xa, 260+ya
yAtaques, yPokemon = 450+ya, 510+ya
# coordenadas x de los ataques
xAtaques = []
for i in range(0, 4):
    xAtaques.append(75 + xa + 160*i)

# corrdenadas x de los pokemon
xPokemon = []
for j in range(0, 6):
    xPokemon.append(45 + xa + 107*j)

# INICIALIZAR
# inicializa lista de pokemons vacia
pokemon = np.empty(0, dtype=Pokemon)

####################### FUNCIONAMIENTO DE TURNO

while True:
    detectarDebilitado()

    leerTodo()
    while espera() == False:
       espera()
 
    mov = best_move(get_move_data(pokemon[0].ataques[0] , moves), get_move_data(pokemon[0].ataques[1], moves),
       get_move_data(pokemon[0].ataques[2], moves), get_move_data(pokemon[0].ataques[3], moves), pokemon[0].atk , pokemon[0].spc , [enemigo.tipos[0] , enemigo.tipos[1]])
    print(mov)
    if mov == 5:
        #cambiarPokemon
         for i in range (0, 5):
             cambiarPokemon(i)
             i+=1
    else:
        seleccionarAtaque(mov)
   
    while espera() == False:
        espera()
   
