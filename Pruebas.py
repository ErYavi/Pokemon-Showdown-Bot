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

im = cv2.imread("WARA.jpg")

print(pytesseract.image_to_string(im))