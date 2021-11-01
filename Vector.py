import math

class Vector():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def vector(self):
        return (self.x, self.y)
        # returns a tuple of the vector 

    def __add__ (self, other):
        if type(other) == tuple:
            return Vector(self.x + other[0], self.y+other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x + other, self.y + other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
        # handles addition 

    def __mul__(self, other):
        if type(other) == tuple:
            return Vector(self.x * other[0], self.y * other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x * other, self.y * other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
        # handles multiplication 

    def __sub__(self, other):
        if type(other) == tuple:
            return Vector(self.x - other[0], self.y - other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x + other, self.y - other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
        # handles substraction 

    def __truediv__(self, other):
        if type(other) == tuple:
            return Vector(self.x / other[0], self.y / other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x / other, self.y / other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
        # handles division 

    def __str__(self) -> str:
        return str((self.x, self.y))
        # returns a string of the object when needed 



def calculateAngleBetweenTwoVectors(vectorA:Vector, vectorB:Vector):
    dotProduct = vectorA.x*vectorB.x + vectorA.y*vectorB.y
    modOfVector1 = math.sqrt( vectorA.x*vectorA.x + vectorA.y*vectorA.y)*math.sqrt(vectorB.x*vectorB.x + vectorB.y*vectorB.y) 
    angle = dotProduct/modOfVector1
    angleInDegree = math.degrees(math.acos(angle))
    return angleInDegree

def calculateDistanceBetweenTwoVectors(a:Vector, b:Vector):
    distance = math.sqrt(((b.x - a.x)**2) + ((b.y - a.y)**2))
    return distance

if __name__ == "__main__":
    print(calculateAngleBetweenTwoVectors(Vector(10, 10), Vector(10, 20)))
    print(calculateDistanceBetweenTwoVectors(Vector(10, 10), Vector(-69, 500)))