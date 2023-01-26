import numpy as np
import cv2
from PIL import ImageGrab, ImageOps, Image
import pyautogui as py
import time
import win32gui, win32ui
import win32api, win32con
from pytesseract import *
import pyocr, pyocr.builders
import math
from Objetos import *

# Coordenadas de la esquina superior izquierda del cuadrado
x1, y1 = 0, 125
# Coordenadas de la esquina inferior derecha del cuadrado
x2, y2 = 640, 656

#COGE LA PARTE DE LA PANTALLA DEL COMBATE
#imgOriginal = cv2.imread('prueba1.jpg', cv2.IMREAD_COLOR)
#img = imgOriginal[125:656,0:640]
#imgray = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)
#cv2.imshow("imagen", imgray)

nPokemon = 6
nPokemonRival = 6

#Coordenadas para leer datos pokemon
x, y = 250, 450
#while True:            #
# Take screenshot of specific region
imAntes = np.array(py.screenshot(region=(0, 125, 640, 656)))
win32api.SetCursorPos((x,y))
time.sleep(0.5)
imAtributos = np.array(py.screenshot(region=(0, 125, 640, 656)))
imResta = cv2.subtract(imAntes, imAtributos)
#mask = imResta
#for i in range(imResta):
#    for j in range(imResta):
#        if imResta == 0:
#            mask[i][j] = 0
im = Image.fromarray(imResta)
im.show()

#guardar datos
pytesseract.tesseract_cmd = r'C:\Users\danis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
texto = pytesseract.image_to_string(imResta, lang = 'eng')
print(texto)

def encontrarDato(s):
    i = texto.rfind(s)
    j=4
    dato = ""
    while ("0" <= texto[i+j] <= "9") or texto[i+j] == "." :
        dato +=  texto[i+j]
        j+=1

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
#j=4
#ataque = ""
#while "0" <= texto[i+j] <= "9":
#    ataque +=  texto[i+j]
#    j+=1
#print("Atk =" + ataque)
#ataque = int(ataque)


#if int(texto[i+4])<=9 and int(texto[i+4])>=0:
#    numero1 = int(texto[i+4])
#    if int(texto[i+5]) <=9 and int(texto[i+5])>=0:
#        numero2 = int(texto[i+5])
#        if int(texto[i+6]) <=9 and int(texto[i+6])>=0:
#            numero3 = int(texto[i+6])
#        else: numero3 = None
#    else: numero2 = None
#
#atq = int(numero1, numero2, numero3)
#print(atq) 


#img_blur = cv2.GaussianBlur(imResta, (5, 5), 0)

# Convertir a escala de grises
#gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# Encontrar los contornos de la imagen
#contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Buscar el contorno del rectángulo con esquinas curvas
#for cnt in contours:
#    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
#    if len(approx) == 4:
#        cv2.drawContours(imResta, [approx], 0, (0, 0, 255), 2)

# Mostrar la imagen con el rectángulo dibujado
#cv2.imshow(imResta)
#cv2.waitKey()






## Display screenshot
#im.show()
#cv2.waitKey()
#
#
#cv2.imshow("imagen", im)
#cv2.waitKey()
#
##
##imgray 
##canny = cv2.Canny(imgray, 100, 200)
##cv2.imshow("canny", canny)
##contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
##imdraw = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
##for cnt in contornos:
##    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
##    if len(approx) == 4:
##        x, y, w, h = cv2.boundingRect(cnt)
##        cv2.drawContours(imdraw, cnt, -1, (0, 255, 0), 8)
##        if abs (w - h) > 5:
##            cv2.drawContours (imdraw, cnt, -1, (0, 0, 255), 8
#
#


## Dibuja el cuadrado
#dc = win32gui.GetDC(0)
#dcObj = win32ui.CreateDCFromHandle(dc)
#hwnd = win32gui.WindowFromPoint((0,0))
#monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
#
#while True:
#    m = win32gui.GetCursorPos()
#    dcObj.Rectangle((m[0], m[1], m[0]+30, m[1]+30))
#    win32gui.InvalidateRect(hwnd, monitor, True) # Refresh the entire monitor
###calcularArea()

# #cuadrado = py.drawRectangle((x1, y1), (x2, y2), width=2)

##class ataque:
##    def __init__(tipo, daño, precision, estado):
##        self.tipo = tipo
##        self.daño = daño
##        self.precision = precision
##        self.estado = None