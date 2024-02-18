# Vector

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x, y = self.x + other.x, self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x, y = self.x - other.x , self.y - other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        x, y = self.x * self.scalar, self.y * self.scalar
        return Vector(x, y)

    def distance(self, other):
        # distance return as a float
        distance = ((abs(self.x - other.x))**2 + (abs(self.y - other.y))**2)**0.5
        return distance

if __name__ == "__main__":
    a = Vector(0, 0)
    b = Vector(1, 1)
    c = a+b
    type(c) == Vector
