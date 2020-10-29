import cv2
import numpy as np


def dilatation(image):
    """
    création du filtre de dilatation
    :param image: dossier imlage
    :return: filtre de dilatation
    """
    kernel = np.ones((5, 5,), np.uint8)
    dlt = cv2.dilate(image, kernel, iterations=1)
    return dlt

