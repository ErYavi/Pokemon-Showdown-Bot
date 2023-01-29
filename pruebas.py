import cv2

# Cargar imagen y plantilla
img = cv2.imread('beedrill.jpg')
template = cv2.imread('templates/bug.jpg')

# Escalar plantilla
# aumenta la plantilla 10 veces
template = cv2.resize(template, (0, 0), fx=31/255, fy=11/95)

# Buscar plantilla en imagen
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# Encuentra la mejor coincidencia
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# Dibuja un rectángulo en la ubicación de la mejor coincidencia
if max_val > 0.55:
    top_left = (max_loc[0], max_loc[1])
    bottom_right = (top_left[0] + template.shape[1],
                    top_left[1] + template.shape[0])
    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

# Muestra la imagen con el rectángulo
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
