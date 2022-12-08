import numpy as np
from schema import INPUT_SHAPE

def convertImage(image):
    """
    Convert an image from MongoDB (stored in json format)
    to a 2D numpy array
    """
    pixels = np.zeros(INPUT_SHAPE)
    for key in image.keys():
        if key not in ("_id", "label"):
            row, col = key.split("x")
            pixels[int(row)-1][int(col)-1] = image[key]
    return pixels/255