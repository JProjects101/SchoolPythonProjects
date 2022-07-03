#Version: Python 3.9
#Description: This program will design a class named Shape with two functions. 
#Description: Two functions will cover area and volume with return value of zero. 
#Desciption: It will calculate the points of x and y.  Giving us the area circle from a point with a public inheritance.
#Desciption: Finally, the cylinder will create the one point and one circle to give us the area and volume of a set of functions to return a height. 

import math


#we need to shapre the class definition
class Shape:
	#this is where the shape classes methods are defined 
    def printShapeName(self):
        print('Print shape name mathod')

    def print(self):
        print('Print method')

	#area method is defined as 0
    def area(self):
        return 0

	#area method is returning as 0
    def volume(self):
        return 0


#this is where the class definition is inheriting a shape
class Point(Shape):

        def __init__(self):
            self.__x=0
            self.__y=0


        def __init__(self,x,y):
            self.__x=x
            self.__y=y


#this is where the defining inhertance come from a circle
class Circle(Point):

    def __init__(self):
        self.radius=0

    def __init__(self,radius):
        self.radius=radius

    def setRadius(self,radius):
        self.radius=radius

    def getRadius(self,radius):
        return self.radius

    def area(self):
        return math.pi*(self.radius**2)

#this is where cylinders are class definitions of interiting cirlces
class Cylinder(Circle):

    def __init__(self):
        self.height=0

    def __init__(self,radius,height):
        self.height=height
        super().__init__(radius)

def getHeight(self):
        return self.height

def setHeight(self,height):
    self.height=height

def area(self):
    return 2*math.pi*self.radius*self.height+2*math.pi*(self.radius**2)

def volume(self):
    return math.pi*(self.radius**2)*self.height

#we then create a point object and call for shape methods
point=Point(1,2)
point.printShapeName()
point.print()

#this is he circle object with calling of area and volumes
circle=Circle(5)
print('Area of circle',circle.area())
print('Volume of circle',circle.volume())

#we then create the cylinder object and call the area and volume methods
cylinder=Cylinder(2,3)
print('Area of cylinder',cylinder.area())
print('Volume of cylinder',cylinder.volume())

Output:

Print shape name method
Print method
Area of circle 78.53981633974483
Volume of circle 0
Area of cylinder 12.566370614359172
Volume of cylinder 0

Process finished with exit code 0



