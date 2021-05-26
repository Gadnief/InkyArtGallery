import requests
import json
import random

def getAllImageIds():
    result = requests.get('https://api.smk.dk/api/v1/art/all_ids').content
    return json.loads(result)['objectIDs']


def selectRandomImage(imageList):
    resultimage = None
    while True:
        imageID = imageList[random.randint(0, len(imageList)-1)]
        result = requests.get('https://api.smk.dk/api/v1/art/?object_number={objectNumber}&lang=en'.format(objectNumber=imageID)).content

        if(json.loads(result)['items'][0]['has_image'] == True):
            resultimage = json.loads(result)
            break

    return resultimage


def downloadImage(imageInfo):
    url = imageInfo['items'][0]['image_native']
    return url
