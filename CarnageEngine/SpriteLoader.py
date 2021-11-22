from PIL import Image
import PIL
from pygame import Rect, image
import io

"""
Development postponed
"""
class ProcessImage():
    def __init__(self, filePath:str, size=1):
        """
        Processes image according to the needs and
        returns a pygame surface
        Set the 'size' Parameter to False if resizing not needed
        """
        if size:
            if type(size) == tuple:
                self.image = Image.open(filePath).resize(size)
            elif type(size) == int or type(size) == float:
                i = Image.open(filePath)
                self.image = i.resize((int(i.width * size), int(i.height * size)))
            # loading the image and resizing if needed 
        else:
            self.image = Image.open(filePath)
            # loading the image 
        
        
        self.getSurface(True)
        # getting the image as a pygame surface 
    def getSurface(self, updateSurface = False):
        spriteSize = list(self.image.size)
        # getting the size of the sprite 
        
        pixelList = {}
        # initialisng a list for all pixels

        for x in range(0, spriteSize[0]):
            for y in range(0, spriteSize[1]):
                """
                Looping through the image
                """
                color = self.image.getpixel((x,y))
                # getting the color of the pixel  

                pixelList[(x,y)] = color

        return (pixelList, tuple(spriteSize))