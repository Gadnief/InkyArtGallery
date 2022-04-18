import json
from configparser import ConfigParser
import hashlib
import random
import requests

config = ConfigParser()
config.read('config.ini')

private_key = str(config.get('marvel', 'private_key'))
public_key = str(config.get('marvel', 'public_key'))
ts = str(config.get('marvel', 'ts'))
api_hash = hashlib.md5(str(ts + private_key + public_key).encode()).hexdigest()

def getAllImageIds():
    print('Fetching all ids in marvel api not needed!')
    return 0

def selectRandomImage(id):
    imageID = random.randint(0, 50000 - 1)
    print(imageID)
    result = requests.get(
        'http://gateway.marvel.com/v1/public/comics/{imageID}?apikey={apikey}&ts=1&hash={hash}'.format(imageID=imageID,
                                                                                                       apikey=public_key,
                                                                                                       hash=api_hash))
    if result.status_code != 200:
        selectRandomImage(0)
    else:
        imageInfo = {}
        imageInfo['primaryImage'] = json.loads(result.content)['data']['results'][0]['images'][0]['path']
        imageInfo['title'] = json.loads(result.content)['data']['results'][0]['title']
        return imageInfo

def downloadImage(imageInfo):
    imagemeta = {}
    imagemeta['url'] = imageInfo['primaryImage']
    imagemeta['title'] = imageInfo['title']
    return imagemeta