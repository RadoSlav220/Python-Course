from cmath import pi


class Rectangle:
    def __init__(self, length, width, color):
        self.__length = length
        self.__width = width
        self.__color = color

    @property
    def length(self):
        return self.__length
    
    @property
    def  width(self):
        return self.__width
    
    @property
    def color(self):
        return self.__color
    
    def area(self):
        return self.__length * self.__width
    
    def __str__(self):
        return f"Rectangle: {self.length=}, {self.width=}, {self.color=}"


class Circle:
    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = color

    @property
    def radius(self):
        return self.__radius
    
    @property
    def color(self):
        return self.__color
    
    def area(self):
        return pi * self.__radius ** 2
    
    def __str__(self):
        return f"(Circle: {self.radius=}, {self.color=}"
    

class Shapes:
    def __init__(self):
        self.__shapes = []

    def addRectangle(self, rectangle):
        self.__shapes.append(rectangle)

    def addCircle(self, circle):
        self.__shapes.append(circle)

    def rectanglesAreas(self):
        rectanglesAreasSum = 0
        for shape in self.__shapes:
            if isinstance(shape, Rectangle):
                rectanglesAreasSum += shape.area()
        return rectanglesAreasSum
    
    def circlesAreas(self):
        circlesAreasSum = 0
        for shape in self.__shapes:
            if isinstance(shape, Circle):
                circlesAreasSum += shape.area()
        return circlesAreasSum

    def getShapeByIndex(self, index):
        return self.__shapes[index]    
    
shapes = Shapes()
shapes.addRectangle(Rectangle(3, 4, "blue"))
shapes.addCircle(Circle(3, "red"))
shapes.addCircle(Circle(1, "black"))

print(f"{shapes.rectanglesAreas()=}")
print(f"{shapes.circlesAreas()=}")
print(f"{shapes.getShapeByIndex(0)}")
print(f"{shapes.getShapeByIndex(2)=}")
print(f"{shapes.getShapeByIndex(2)}")
