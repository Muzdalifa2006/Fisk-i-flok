class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __add__(self, other):
        return Vector(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other):
        return Vector(self.__x - other.x, self.__y - other.y)
    
    def __mul__(self, k):
        return Vector(self.__x * k, self.__y * k)
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def getLength(self):
        return ((self.__x * self.__x) + (self.__y * self.__y))**0.5
    
    def normalize(self):
        length = self.getLength()
        normalize = Vector(self.__x / length, self.__y / length)
        return normalize
    