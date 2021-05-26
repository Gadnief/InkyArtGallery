import smk_gallery
import meetmuseum_gallery

import random

galleries = []
galleries.append(smk_gallery)
#galleries.append(meetmuseum_gallery)
gallery = galleries[random.randint(0,len(galleries)-1)]

imagelist = gallery.getAllImageIds()
imageInfo = gallery.selectRandomImage(imagelist)
print(gallery.downloadImage(imageInfo))