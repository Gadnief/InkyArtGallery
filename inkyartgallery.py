import smk_gallery
import meetmuseum_gallery
from inky.inky_uc8159 import Inky
from PIL import Image

import random

print('starting')
galleries = []
galleries.append(smk_gallery)
#galleries.append(meetmuseum_gallery)
gallery = galleries[random.randint(0,len(galleries)-1)]

imagelist = gallery.getAllImageIds()
imageInfo = gallery.selectRandomImage(imagelist)

board = Inky()
print('board setup')
image = Image.open(gallery.downloadImage(imageInfo))
board.set_image(image)
board.show()
print('done!')