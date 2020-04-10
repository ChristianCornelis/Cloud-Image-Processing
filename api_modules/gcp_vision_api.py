import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def call_vision():
    '''
    Calls on the Google Vision API, using all files within the resources folder as paramaters.
    '''
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    directory = './resources/'

    # Iterate over each image in the resources directory, outputting labels for each.
    for filename in os.listdir(directory):
        with io.open(os.path.join('resources', filename), 'rb') as image_file:
            content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            print(filename + ' Labels:')
            for label in labels:
                print('\t' + label.description + ' (' + ("%.2f" % (label.score * 100)) +'% confidence)')