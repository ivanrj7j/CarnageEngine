from PIL import Image
from pygame import image
import io

class ProcessImage():
    def __init__(self, filePath:str, size):
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
                self.image = i.resize((int(i.width / size), int(i.height / size)))
            # loading the image and resizing if needed 
        else:
            self.image = Image.open(filePath)
            # loading the image 
        
        
        self.getSurface(True)
        # getting the image as a pygame surface 
    def getSurface(self, updateSurface = False):
        if updateSurface:
            img_byte_arr = io.BytesIO()
            self.image.save(img_byte_arr, format='PNG')
            self.surface = image.load(img_byte_arr.getvalue())
        return self.surface

        

a = ProcessImage("../testFiles/frame6104.jpg", 10)
print(a.image)