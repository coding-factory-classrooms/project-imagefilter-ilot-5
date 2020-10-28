import cv2
import logger
import os


def open(image_path):
    # image_path contient img/potter.jpg
    print(image_path)
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    return image


def save(image, outputdir, image_name):
    #on esaye de créer le directory
    try:
        os.mkdir(outputdir)

    #si il y arrive pas à le créer
    except OSError:
        print("Creation fail" + outputdir)

    #alors on crée le directory
    else:
        print("Creation " + outputdir)



    # on enregistre l'image générée dans output/potter.jpg
    cv2.imwrite(outputdir + image_name, image)

