import cv2


def filtre_flou(image):
    """
    création du filtre flou
    :param image: dossier image
    :return: filtre flou
    """
    flou = cv2.GaussianBlur(image, (5,5), 0)
    return flou
