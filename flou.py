import cv2
import logger
import os


def filtre_flou(image_path):
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    flou = cv2.GaussianBlur(image, (5,5), 0)

    img_name = os.path.basename(image_path)

    output_path = "output/" + img_name
    print(output_path)

    cv2.imwrite(output_path, flou)

