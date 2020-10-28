import cv2
import logger
import os


def filtre_bw(image_path):
    # image_path contient img/potter.jpg
    print(image_path)
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cvtColor converti l'image en echelle de gris.

    # on extrait le nom de fichier de img/potter.jpg => potter.jpg
    img_name = os.path.basename(image_path)

    # on génère le chemin de sortie => output/potter.jpg
    output_path = "output/" + img_name
    print(output_path)

    # on enregistre l'image générée dans output/potter.jpg
    cv2.imwrite(output_path, gray)
