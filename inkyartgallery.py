import smk_gallery
import meetmuseum_gallery
from inky.inky_uc8159 import Inky
from PIL import Image
import urllib.request

import random

print('starting')
galleries = []
galleries.append(smk_gallery)
#galleries.append(meetmuseum_gallery)
gallery = galleries[random.randint(0,len(galleries)-1)]

imagelist = gallery.getAllImageIds()
imageInfo = gallery.selectRandomImage(imagelist)

urllib.request.urlretrieve(gallery.downloadImage(imageInfo), "gfg.png")

board = Inky()
print('board setup')
image = Image.open("gfg.png").resize((600,448))
board.set_image(image)
board.show()
print('done!')