import smk_gallery
import meetmuseum_gallery
from inky.inky_uc8159 import Inky
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFont
import urllib.request
import random

from font_source_sans_pro import SourceSansProSemibold

print('starting')
galleries = []
#galleries.append(smk_gallery)
galleries.append(meetmuseum_gallery)
gallery = galleries[random.randint(0,len(galleries)-1)]

imagelist = gallery.getAllImageIds()
imageInfo = gallery.selectRandomImage(imagelist)

downlaodedimage = gallery.downloadImage(imageInfo)
url = downlaodedimage['url']
title = downlaodedimage['title']
urllib.request.urlretrieve(url, "gfg.png")

board = Inky()
print('board setup')

rawimage = Image.open("gfg.png").transpose(Image.TRANSPOSE).resize((600,448))
image = ImageOps.flip(rawimage)
filter = ImageEnhance.Color(image)
filteredImage = filter.enhance(1.5)
contrast = ImageEnhance.Contrast(filteredImage)
contrastedImage = contrast.enhance(1.5)

# Draw url
draw = ImageDraw.Draw(contrastedImage)
draw.multiline_text((1, 1), title, fill=board.BLACK, font=ImageFont.truetype(SourceSansProSemibold, 24), align="left")

print('Image loaded')
print('URL: ' + url)
board.set_image(contrastedImage)
print('Try to show')
board.show()
print('done!')