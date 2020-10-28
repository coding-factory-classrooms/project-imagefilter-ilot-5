import black_white
import flou
import dilate
import os
import fonctions

image_list = os.listdir("img")

for f in image_list:
    print(f)

    img = fonctions.open("img/" + f)

    img = black_white.filtre_bw(img)
    img = dilate.dilatation(img)
    img = flou.filtre_flou(img)

    fonctions.save(img, "output/", f)