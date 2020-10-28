def ecrire_fichier(img):
    f = open("image.log", "a")
    f.write(img + "\n")
    f.close()