import cv2
import pyautogui as ag
import numpy as np
import win32gui as wg
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
    ag.alert(title=title, text=text, button=button)
    win32handles = ag.getWindowsWithTitle(title)
    if win32handles:
        wg.SetForegroundWindow(win32handles[0])


pantalla = cv2.cvtColor(np.array(ag.screenshot()), cv2.COLOR_BGR2RGB)

cv2.namedWindow("screen", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback("screen", dibujar)
while option != "yes":
    img = copy.copy(pantalla)
    if switch == True:
        cv2.rectangle(img, (xa, ya), (xb, yb), (200, 100, 0), 1)
        cv2.imshow("screen", img)
        ag.press("f11")
        option = ag.confirm(
            "Game area correctly selected?\nIt must include all the game screen plus your attacks and pokémon, but must NOT include any fo the browser borders or the PokemonShowDown banner. Otherwise the bot will not work", "Confirm", ["yes", "no"])
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
