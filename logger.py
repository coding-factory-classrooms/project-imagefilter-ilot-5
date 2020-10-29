def ecrire_fichier(img):
    """
    Ecrit dans un nouveau fichier l'action apportée et l'image
    :param img: image
    :return: image + filtre choisit
    """
    f = open("image.log", "a")
    f.write(img + "\n")
    f.close()