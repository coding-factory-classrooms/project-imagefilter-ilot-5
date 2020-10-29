import cv2
import logger
import os


def open(image_path):
    # image_path contient img/potter.jpg
    print(image_path)
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    return image


def check_file_existence(output_folder):
    #on esaye de créer le directory
    try:
        os.mkdir(output_folder)

    # si il n'y en a pas, on crée le directory
    except OSError:
        print("Creation " + output_folder)

    # si il y arrive pas à le créer
    else:
        print("Creation fail " + output_folder)

def fichier(file_path):
    f = os.path.exists(file_path)
    return f

    # on enregistre l'image générée dans output/potter.jpg
    cv2.imwrite(outputdir + image_name, image)

def save(nom, img):
    cv2.imwrite("img_output/" + nom, img)

