class Vector():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def vector(self):
        return (self.x, self.y)
    def __add__(self, other:tuple):
        return(self.x + other[0], self.y+other[1])
    def __mul__(self, other:tuple):
        return(self.x * other[0], self.y * other[1])
    def __sub__(self, other:tuple):
        return(self.x - other[0], self.y - other[1])
    def __truediv__(self, other:tuple):
        return(self.x / other[0], self.y / other[1])
