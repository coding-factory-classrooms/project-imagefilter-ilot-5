import cv2
import numpy as np


def dilatation(image):
    kernel = np.ones((5, 5,), np.uint8)
    dlt = cv2.dilate(image, kernel, iterations=1)
    return dlt

