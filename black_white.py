import cv2


def filtre_bw(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cvtColor converti l'image en echelle de gris.
    return gray