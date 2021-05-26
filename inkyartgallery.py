import smk_gallery
import meetmuseum_gallery

import random

galleries = []
#galleries.append(smk_gallery)
galleries.append(meetmuseum_gallery)
gallery = galleries[random.randint(0,len(galleries)-1)]

print(gallery)

imagelist = gallery.getAllImageIds()
imageInfo = gallery.selectRandomImage(imagelist)
print(gallery.downloadImage(imageInfo))

#imagelist = smk_gallery.getAllImageIds()
#imageInfo = smk_gallery.selectRandomImage(imagelist)
#print(smk_gallery.downloadImage(imageInfo))

#imagelist = meetmuseum_gallery.getAllImageIds()
#imageInfo = meetmuseum_gallery.selectRandomImage(imagelist)
#print(meetmuseum_gallery.downloadImage(imageInfo))