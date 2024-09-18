from abc import ABC,abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self, width ,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class square(shape):
    def __init__(self,height):
        self.height = height

    def area(self):
        return self.height * self.height

rectang = Rectangle(4,5)
triang = triangle(3,4)
sq = square(4)
print(f"area of rectangle {rectang.area()}")
print(f"area of triangle {triang.area()}")
print(f"area of square {sq.area()}")
