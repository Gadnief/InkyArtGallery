## https://metmuseum.github.io

import requests
import json
import random

def getAllImageIds():
    result = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=Paintings').content
    return json.loads(result)['objectIDs']


def selectRandomImage(imageList):
    imageID = imageList[random.randint(0, len(imageList)-1)]
    result = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectNumber}'.format(objectNumber=imageID)).content
    if(len(json.loads(result)['primaryImage']) is None):
        selectRandomImage(imageList)
    else:
        return json.loads(result)


def downloadImage(imageInfo):
    url = imageInfo['primaryImage']
    return url
