import pygame
from SpriteLoader import ProcessImage

"""
Development postponed
"""
class Sprite():
    def __init__(self, pixelScanList:tuple):
        """
        The Sprite class, handles all the operations related to sprites except the loading
        use SpriteLoader.ProcessImage() for loading the image as a sprite

        # Use the returned value of the SpriteLoader.ProcessImage().getSurface() as
        the pixelScanList argument
        """
        self.pixelScanList = pixelScanList
        self.rectList = self.loadPixelScanList(pixelScanList=self.pixelScanList)
        print(self.rectList)

    def loadPixelScanList(self, pixelScanList):

        rectangleList = {}
        # the list of all pixelin pygame rectangles 

        for x in range(pixelScanList[1][0]):
            for y in range(pixelScanList[1][1]):
                rectangleList[(x,y)] = [pygame.Rect(x,y,1,1), pixelScanList[0]]

        return rectangleList
                
a = ProcessImage("../testFiles/sonic.png")
sprite = Sprite(a.getSurface())