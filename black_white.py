import cv2


def filtre_bw(image):
    """
    création du filtre noir et blanc
    :param image: dossier image
    :return: filtre noir & blanc
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #cvtColor converti l'image en echelle de gris.
    return gray