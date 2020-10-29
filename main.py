import black_white
import flou
import dilate
import os
import fonctions
import sys

image_list = os.listdir("img")

for f in image_list:
    print(f)

    #ouvre image
    img = fonctions.open("img/" + f)

    args = sys.argv
    print(args)
    for i in range(1, len(args)):
        if args[i] == "dil":
            print("Filtre de dilatation ")
            img = dilate.dilatation(img)

        if args[i] == "flou":
            print("Filtre de flou ")
            img = flou.filtre_flou(img)

        if args[i] == "bw":
            print("Filtre noir et blanc ")
            img = black_white.filtre_bw(img)

        else:
            print("Ce filtre n'existe pas")

    #enregistre image modifiée
    fonctions.save(img, "output/", f)