import numpy as np
import cv2
from PIL import ImageGrab, ImageOps, Image
import pyautogui as py
import time
import win32gui as wg
import win32ui
import win32api
import win32con
from pytesseract import *
import pyocr
import pyocr.builders
import math
from ObjetosBien import *
import copy
import moves
import tipos
import eleccionMovimiento

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

    enemigo = Pokemon(encontrarDato("HP", texto2), None, None, None, None, None)
    return enemigo


def cambiarPokemon(cambio):
    win32api.SetCursorPos((xPokemon[cambio], yPokemon))
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
# lee pokemon actual


def leerTodo():
    global pokemon

    pokemon = np.append(pokemon, (leerActual(x, y)))
    print("# POKEMON ACTUAL: #")
    pokemon[0].mostrar()
    # lee banquillo
    print("# POKEMONS EN EL BANQUILLO #")
    leerBanquillo(pokemon)
    # lee enemigo
    print("# POKEMON ENEMIGO #")
    enemigo = LeerPokemonEnemigo()
    enemigo.mostrar()


def espera():
    wait = py.screenshot(region=(xa + 0, 400 + ya, 640, 140))
    texto0 = pytesseract.image_to_string(wait)
    if "Waiting for opponent..." in texto0:
        time.sleep(1)
        return False
    else:
        return True


# FUNCIONAMIENTO DE TURNO


while True:
   leerTodo()
   break
   #if eleccionMovimiento.best_move()

   
   
   
   
   
   
   
#   for i in range (0, 6):
#
#   for j in range (0, 4):
#       pokemon[i].ataques = leerAtaque(texto)
#

# PRUEBAS
# pruebas de las coordenadas
# for i in range (0 , 4):
#    print(xAtaques[i])
#
# for j in range (0, 6):
#    print(xPokemon[j])
#
#win32api.SetCursorPos((x, y))
# time.sleep(0.5)
#
# va poniendo el cursor en las coordenadas
# for i in range (0, 4):
#    win32api.SetCursorPos((xAtaques[i], yAtaques))
#    time.sleep(0.5)
#
# for j in range (0, 6):
#    win32api.SetCursorPos((xPokemon[j], yPokemon))
#    time.sleep(0.5)
#
#
#screen = py.screenshot(region=(xa, ya, xb-xa, yb-ya))
# screen.show()
#
#pytesseract.tesseract_cmd = r'C:\Users\danis\AppData\Local\Programs\Tesseract-OCR\tesseract'

# template matching
# def match_template(image, template):
#    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
