import black_white
import flou
import dilate
import os
import fonctions
import sys

args = sys.argv

for i in range (0, len(args)):
    if args[i] == "-i":
        input_folder = args[i + 1]
    if args[i] == "-o":
        output_folder = args[i + 1]

folder = fonctions.fichier(output_folder)
image_list = os.listdir(input_folder)

if not folder:
    fonctions.check_file_existence(output_folder)

for f in image_list:
    print(f)

    #ouvre image
    img = fonctions.open("img/" + f)

    args = sys.argv
    print(args)
    for i in range(0, len(args)):
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
    fonctions.save("test.jpg", img)