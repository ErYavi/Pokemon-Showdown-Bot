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
from Objetos import *
import copy

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

nPokemon = 6
nPokemonRival = 6

# Coordenadas para leer datos pokemon
x, y = 200+xa, 278+ya
win32api.SetCursorPos((x, y))
time.sleep(2)
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

#i = texto.rfind('Atk')
# j=4
#ataque = ""
# while "0" <= texto[i+j] <= "9":
#    ataque +=  texto[i+j]
#    j+=1
#print("Atk =" + ataque)
#ataque = int(ataque)


# if int(texto[i+4])<=9 and int(texto[i+4])>=0:
#    numero1 = int(texto[i+4])
#    if int(texto[i+5]) <=9 and int(texto[i+5])>=0:
#        numero2 = int(texto[i+5])
#        if int(texto[i+6]) <=9 and int(texto[i+6])>=0:
#            numero3 = int(texto[i+6])
#        else: numero3 = None
#    else: numero2 = None
#
#atq = int(numero1, numero2, numero3)
# print(atq)


#img_blur = cv2.GaussianBlur(imResta, (5, 5), 0)

# Convertir a escala de grises
#gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# Encontrar los contornos de la imagen
#contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Buscar el contorno del rectángulo con esquinas curvas
# for cnt in contours:
#    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
#    if len(approx) == 4:
#        cv2.drawContours(imResta, [approx], 0, (0, 0, 255), 2)

# Mostrar la imagen con el rectángulo dibujado
# cv2.imshow(imResta)
# cv2.waitKey()


# Display screenshot
# im.show()
# cv2.waitKey()
#
#
#cv2.imshow("imagen", im)
# cv2.waitKey()
#
##
# imgray
##canny = cv2.Canny(imgray, 100, 200)
##cv2.imshow("canny", canny)
##contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
##imdraw = cv2.cvtColor(canny, cv2.COLOR_GRAybBGR)
# for cnt in contornos:
##    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
# if len(approx) == 4:
##        x, y, w, h = cv2.boundingRect(cnt)
##        cv2.drawContours(imdraw, cnt, -1, (0, 255, 0), 8)
# if abs (w - h) > 5:
# cv2.drawContours (imdraw, cnt, -1, (0, 0, 255), 8
#
#


# Dibuja el cuadrado
#dc = win32gui.GetDC(0)
#dcObj = win32ui.CreateDCFromHandle(dc)
#hwnd = win32gui.WindowFromPoint((0,0))
#monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
#
# while True:
#    m = win32gui.GetCursorPos()
#    dcObj.Rectangle((m[0], m[1], m[0]+30, m[1]+30))
#    win32gui.InvalidateRect(hwnd, monitor, True) # Refresh the entire monitor
# calcularArea()

# #cuadrado = py.drawRectangle((xa, ya), (xb, yb), width=2)

# class ataque:
# def __init__(tipo, daño, precision, estado):
##        self.tipo = tipo
##        self.daño = daño
##        self.precision = precision
##        self.estado = None
