import cv2
import black_white
import flou
import dilate


b = black_white.filtre_bw('img/harryPotter.jpg')
f = flou.filtre_flou('img/joker.jpg')
d = dilate.dilatation('img/jumanji.jpg')