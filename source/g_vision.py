from google.cloud import vision
from google.cloud.vision import types
import requests

class Image():
    def __init__(self,objects):
        self.objects = self.parseObjects(objects)
    
    def parseObjects(self,objectList):
        objects = []
        for item in objectList:
            objects.append({'name':item.name,'score':item.score})
        return objects



def getImageDescription(url):
    if len(url) == 0:
        return None
    content = requests.get(url, stream=True).content
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    objects = client.object_localization(image=image).localized_object_annotations
    return Image(objects)