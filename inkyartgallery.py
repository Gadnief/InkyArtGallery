import requests
import json
import random

def getAllImageIds():
    result = requests.get('https://api.smk.dk/api/v1/art/all_ids').content
    return json.loads(result)['objectIDs']


def selectRandomImage(imageList):
    imageID = imageList[random.randint(0, len(imageList))]
    result = requests.get('https://api.smk.dk/api/v1/art/?object_number={objectNumber}&lang=en'.format(objectNumber=imageID)).content
    return json.loads(result)


def downloadImage(imageInfo):
    url = imageInfo['items'][0]['image_native']
    print(url)


imagelist = getAllImageIds()
imageInfo = selectRandomImage(imagelist)
downloadImage(imageInfo)