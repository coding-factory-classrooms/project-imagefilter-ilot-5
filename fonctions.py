import cv2
import logger
import os
import sys

args = sys.argv
#recupere arguments

for i in range(0, len(args)):
    #reccupere dossier output
    if args[i] == "-o":
        output_folder = args[i + 1]

def open(image_path):
    """
    Ouvre image
    :param image_path: chemin de l'image
    :return: chemin de l'image et le filtre
    """
    print(image_path)
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    return image


def check_file_existence(output_folder):
    """
    Verification de output
    :param output_folder: dossier output ???
    :return: creation du fichier si il n'est pas present
    """
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
    """
    on enregistre l'image générée dans output/
    :param file_path: chemin du fichier
    :return: f= image
    """
    f = os.path.exists(file_path)
    return f

    cv2.imwrite(outputdir + image_name, image)

def save(nom, img):
    """
    sauvegarde de l'image modifiée dans le output/
    :param nom: nom image
    :param img: image de base
    :return: image modifiée
    """
    cv2.imwrite(output_folder + "/" + nom, img)

