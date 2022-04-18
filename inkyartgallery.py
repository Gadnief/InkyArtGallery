import smk_gallery
import meetmuseum_gallery
import marvel_gallery
from inky.inky_uc8159 import Inky
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFont
import urllib.request
import random

title = ""

def downloadValidImage():
    while True:
        ratio = 1
        try:
            print('Downloading image')
            galleries = []
            # galleries.append(smk_gallery)
            # galleries.append(meetmuseum_gallery)
            galleries.append(marvel_gallery)
            gallery = galleries[random.randint(0, len(galleries) - 1)]

            imagelist = gallery.getAllImageIds()
            imageInfo = gallery.selectRandomImage(imagelist)

            downlaodedimage = gallery.downloadImage(imageInfo)
            url = downlaodedimage['url']
            print('URL: ' + url)
            title = downlaodedimage['title']
            print('Title: ' + title)
            urllib.request.urlretrieve(url, "gfg.png")

            rawimage = Image.open("gfg.png")
            ratio = (rawimage.width / rawimage.height)
        except:
            print ('Error getting image! Retry!')


        if ratio < 2 and ratio > 0.1:
            print ('Found Image!')
            return (rawimage, title)
        else:
            print ('Invalid image ratio! Retry!')



print('starting')

board = Inky()
print('board setup')

imageinfo = downloadValidImage()
rawimage = imageinfo[0]
title = imageinfo[1]

print('Transposing image')
transposedImage = rawimage.transpose(Image.TRANSPOSE).resize((600,448))
image = ImageOps.flip(transposedImage)
filter = ImageEnhance.Color(image)
filteredImage = filter.enhance(1.5)
contrast = ImageEnhance.Contrast(filteredImage)
contrastedImage = contrast.enhance(1.5)

print('Image loaded')
board.set_image(contrastedImage)

print('Try to show')
board.show()
print('DONE!')

