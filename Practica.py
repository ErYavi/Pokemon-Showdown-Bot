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

################################################################
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
print("sin ordenar:\n("+str(xa)+", "+str(ya)+")("+str(xb)+", "+str(yb)+")")

if xa > xb:
    aux = copy.copy(xa)
    xa = copy.copy(xb)
    xb = copy.copy(aux)
if ya > yb:
    aux = copy.copy(ya)
    ya = copy.copy(yb)
    yb = copy.copy(aux)

print("ordenadas:\n("+str(xa)+", "+str(ya)+")("+str(xb)+", "+str(yb)+")")

#coordenada para tapar chat
xChat, yChat = 700 + xa, 16 + ya
win32api.SetCursorPos((xChat, yChat))
py.click()

# Coordenadas para leer datos pokemon
x, y = 200+xa, 260+ya
yAtaques, yPokemon = 450+ya, 510+ya
#coordenadas x de los ataques
xAtaques = []
for i in range (0 , 4):
    xAtaques.append(75 + xa + 160*i) 

#corrdenadas x de los pokemon
xPokemon = [] 
for j in range (0, 6):
    xPokemon.append(45 + xa + 107*j)

#pruebas de las coordenadas
for i in range (0 , 4):
    print(xAtaques[i])

for j in range (0, 6):
    print(xPokemon[j])

win32api.SetCursorPos((x, y))
time.sleep(0.5)

#va poniendo el cursor en las coordenadas
for i in range (0, 4):
    win32api.SetCursorPos((xAtaques[i], yAtaques))
    time.sleep(0.5)

for j in range (0, 6):
    win32api.SetCursorPos((xPokemon[j], yPokemon))
    time.sleep(0.5)

screen = py.screenshot(region=(xa, ya, xb-xa, yb-ya))
screen.show()

# guardar datos
texto = pytesseract.image_to_string(screen, lang='eng')
print(texto)

def encontrarDato(s):
    i = texto.rfind(s)
    j = 4
    dato = ""
    while ("0" <= texto[i+j] <= "9") or texto[i+j] == ".":
        dato += texto[i+j]
        j += 1

    return dato

print("---PRUEBAS DE ATRIBUTOS CAPTURADOS---")
vida = encontrarDato("HP")
print(vida)
ataque = encontrarDato("Atk")
print(ataque)
defensa = encontrarDato("Def")
print(defensa)
especial = encontrarDato("Spc")
print(especial)
velocidad = encontrarDato("Spe")
print(velocidad)

pokemon = Pokemon(vida, ataque, defensa, especial, velocidad)
print(pokemon)

#########################################################################
pytesseract.tesseract_cmd = r'C:\Users\danis\AppData\Local\Programs\Tesseract-OCR\tesseract'

def encontrarNombre():
    i = 0
    while texto[i] != " ":
        nombre = texto[0:i]
        i += 1
    return nombre

def encontrarDato(s):
    i = texto.rfind(s)
    j=4
    dato = ""
    while ("0" <= texto[i+j] <= "9") or texto[i+j] == "." :
        dato +=  texto[i+j]
        j+=1
    return dato

##template matching
#def match_template(image, template):
#    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

print("---ATRIBUTOS CAPTURADOS---")
nombre = encontrarNombre()
print(nombre)
vida = encontrarDato("-HP")
print(vida)
ataque = encontrarDato("-Atk")
print(ataque)
defensa = encontrarDato("-Def")
print(defensa)
especial = encontrarDato("-Spc")
print(especial)
velocidad = encontrarDato("-Spe")
print(velocidad)
pokemonActual = Pokemon(nombre, vida, ataque, defensa, especial, velocidad)

#print("--ATAQUES CAPTURADOS---")
#ataques = np.array(imAntes[405:445][15:622])
#ataques = Image.fromarray(ataques)
#ataques.show()
textoAtaques = pytesseract.image_to_string(ataques, lang = 'eng')
print(textoAtaques)

# Dividir la frase en una lista de palabras
ataques = textoAtaques.split()


q = 0
for q in q < 4:
    ataque = Ataque(ataques[q])
    pokemonActual.ataques[q] = ataque
