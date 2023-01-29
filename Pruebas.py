import cv2
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

imagen = py.screenshot(region=(0+0, 417+128, 637, 21))
ataques = []
for i in range(0, 4):
    img = imagen.crop((155*i + 10,  0,  155*i + 150, 20))
    ataque = pytesseract.image_to_string(img, lang="eng")
    ataques.append(ataque)

print(ataques)