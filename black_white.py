import cv2
import logger



def filtre_bw(image_path):
    image = cv2.imread(image_path)  # imread
    logger.ecrire_fichier("Ajout du filtre" + image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cvtColor converti l'image en echelle de gris.

    cv2.imshow('Original', image) #imshow affiche l'image
    cv2.imshow('Gray image', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imageSortie =cv2.imwrite(image, image_path)