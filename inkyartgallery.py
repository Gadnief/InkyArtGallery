import smk_gallery
import meetmuseum_gallery
from inky.inky_uc8159 import Inky
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFont
import urllib.request
import random

from font_source_sans_pro import SourceSansProSemibold

def downloadValidImage():
    print('Downloading image')
    galleries = []
    #galleries.append(smk_gallery)
    galleries.append(meetmuseum_gallery)
    gallery = galleries[random.randint(0, len(galleries) - 1)]

    while True:
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

        if (ratio > 1.4):
            return True
        else:
            return True
            # break

    return (rawimage, title)

print('starting')

board = Inky()
print('board setup')

rawimage = downloadValidImage()[0]

print('Transposing image')
transposedImage = rawimage.transpose(Image.TRANSPOSE).resize((600,448))
image = ImageOps.flip(transposedImage)
filter = ImageEnhance.Color(image)
filteredImage = filter.enhance(1.5)
contrast = ImageEnhance.Contrast(filteredImage)
contrastedImage = contrast.enhance(1.5)

# Draw url
draw = ImageDraw.Draw(contrastedImage)
draw.multiline_text((1, 1), rawimage[1], fill=board.WHITE, font=ImageFont.truetype(SourceSansProSemibold, 24), align="left")

print('Image loaded')
print('URL: ' + url)
board.set_image(contrastedImage)
print('Try to show')
board.show()
print('done!')

