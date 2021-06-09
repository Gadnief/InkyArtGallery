import smk_gallery
import meetmuseum_gallery
from inky.inky_uc8159 import Inky

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
board.set_image(gallery.downloadImage(imageInfo))
board.show()
print('done!')