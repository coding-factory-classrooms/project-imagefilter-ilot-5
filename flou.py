import cv2
import logger


def filtre_flou(image_path):
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    flou = cv2.GaussianBlur(image, (5,5), 0)

    cv2.imshow('Original', image)  # imshow affiche l'image
    cv2.imshow('Flou image', flou)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imageSortie = cv2.imwrite(image_path, image)
