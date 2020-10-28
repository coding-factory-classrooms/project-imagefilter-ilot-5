import cv2
import logger
import numpy as np
import os

def dilatation(image_path):
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    kernel= np.ones((5,5,),np.uint8)
    dlt = cv2.dilate(image, kernel, iterations=1)

    img_name = os.path.basename(image_path)

    output_path = "output/" + img_name
    print(output_path)

    cv2.imwrite(output_path, dlt)