import cv2
import black_white
import flou
import dilate
import os

image_list = os.listdir("img")

for img in image_list:
    print(img)
    black_white.filtre_bw("img/"+img)
    dilate.dilatation("img/"+img)
    flou.filtre_flou("img/"+img)