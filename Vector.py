class Vector():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def vector(self):
        return (self.x, self.y)
    def __add__ (self, other):
        if type(other) == tuple:
            return Vector(self.x + other[0], self.y+other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x + other, self.y + other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
    def __mul__(self, other):
        if type(other) == tuple:
            return Vector(self.x * other[0], self.y * other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x * other, self.y * other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
    def __sub__(self, other):
        if type(other) == tuple:
            return Vector(self.x - other[0], self.y - other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x + other, self.y - other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
    def __truediv__(self, other):
        if type(other) == tuple:
            return Vector(self.x / other[0], self.y / other[1])
        elif type(other) == int or type(object) == float:
            return Vector(self.x / other, self.y / other)
        elif type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise(f"Operation not supported with vector and {type(other)}")
    def __str__(self) -> str:
        return str((self.x, self.y))

if __name__ == "__main__":
    pass