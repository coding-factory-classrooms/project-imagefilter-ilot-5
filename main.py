import black_white
import flou
import dilate
import os
import fonctions
import sys

args = sys.argv

for i in range (0, len(args)):
    #récupère les dossier d'input et d'output
    if args[i] == "-i":
        input_folder = args[i + 1]
    if args[i] == "-o":
        output_folder = args[i + 1]
try:
#permet de continuer a faire tourner le programme meme si il y a une erreur
    folder = fonctions.fichier(output_folder)
    image_list = os.listdir(input_folder)
except NameError:
    print("Entrer un paramètre")
    sys.exit(1)

if not folder:
    fonctions.check_file_existence(output_folder)

for f in image_list:
    #ouvre image grace a une fonction
    img = fonctions.open("img/" + f)

    args = sys.argv
    for i in range(0, len(args)):
    #permet de choisir le filtre
        if args[i] == "dil":
            print("Filtre de dilatation ")
            img = dilate.dilatation(img)

        if args[i] == "flou":
            print("Filtre de flou ")
            img = flou.filtre_flou(img)

        if args[i] == "bw":
            print("Filtre noir et blanc ")
            img = black_white.filtre_bw(img)

    #enregistre image modifiée grace a une fonction
        fonctions.save(f, img)
