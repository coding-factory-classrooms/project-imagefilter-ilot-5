import cv2
import logger
import numpy as np


def dilatation(image_path):
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    kernel= np.ones((5,5,),np.uint8)
    dlt = cv2.dilate(image, kernel, iterations=1)

    cv2.imshow('Original', image) #imshow affiche l'image
    cv2.imshow('Dilate image', dlt)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imageSortie =cv2.imwrite(image_path, image)
