import smk_gallery
import meetmuseum_gallery
from inky.inky_uc8159 import Inky
from PIL import Image, ImageOps
import urllib.request

import random

print('starting')
galleries = []
galleries.append(smk_gallery)
galleries.append(meetmuseum_gallery)
gallery = galleries[random.randint(0,len(galleries)-1)]

imagelist = gallery.getAllImageIds()
imageInfo = gallery.selectRandomImage(imagelist)

imageurl = gallery.downloadImage(imageInfo)
urllib.request.urlretrieve(imageurl, "gfg.png")

board = Inky()
print('board setup')
rawimage = Image.open("gfg.png").transpose(Image.TRANSPOSE).resize((600,448))
image = ImageOps.flip(rawimage)

print('Image loaded')
print('URL: ' + imageurl)
board.set_image(image)
print('Try to show')
board.show()
print('done!')