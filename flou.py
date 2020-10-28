import cv2


def filtre_flou(image):
    flou = cv2.GaussianBlur(image, (5,5), 0)
    return flou
