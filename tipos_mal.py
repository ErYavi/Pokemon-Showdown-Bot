def compararTemplate(img, dir):
    template = cv2.imread(dir)
    template = cv2.resize(template, (0, 0), fx=31/255, fy=11/95)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)
    if max_val > 0.6:
        return True
    else:
        return False


def leerTipo(img):
    types = []
    if (compararTemplate(img, tipos.Bug) == True):
        types.append('Bug')
    if (compararTemplate(img, tipos.Dragon) == True):
        types.append('Dragon')
    if (compararTemplate(img, tipos.Electr) == True):
        types.append('Electr')
    if (compararTemplate(img, tipos.Fight) == True):
        types.append('Fight')
    if (compararTemplate(img, tipos.Fire) == True):
        types.append('Fire')
    if (compararTemplate(img, tipos.Flying) == True):
        types.append('Flying')
    if (compararTemplate(img, tipos.Ghost) == True):
        types.append('Ghost')
    if (compararTemplate(img, tipos.Grass) == True):
        types.append('Grass')
    if (compararTemplate(img, tipos.Ground) == True):
        types.append('Ground')
    if (compararTemplate(img, tipos.Ice) == True):
        types.append('Ice')
    if (compararTemplate(img, tipos.Normal) == True):
        types.append('Normal')
    if (compararTemplate(img, tipos.Poison) == True):
        types.append('Poison')
    if (compararTemplate(img, tipos.Psychc) == True):
        types.append('Psychc')
    if (compararTemplate(img, tipos.Rock) == True):
        types.append('Rock')
    if (compararTemplate(img, tipos.Water) == True):
        types.append('Water')
    return types
