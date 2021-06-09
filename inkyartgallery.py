import smk_gallery
import meetmuseum_gallery
from inky.auto import auto

import random

print('starting')
galleries = []
galleries.append(smk_gallery)
#galleries.append(meetmuseum_gallery)
gallery = galleries[random.randint(0,len(galleries)-1)]

imagelist = gallery.getAllImageIds()
imageInfo = gallery.selectRandomImage(imagelist)

board = auto()
print('board setup')
board.set_image(gallery.downloadImage(imageInfo))
print('done!')