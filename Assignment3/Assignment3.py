## Assignment3 ES 122
## Name: Julian Wearden
## EID : jfw864
##
## Fill in the functions and classes below


# Problem 1
# Optional Paramaters:
# Each of these paramaters should have the value True if you are applying the paramater 
# Reverse: Sorts from highest to lowest.
# NoDuplicates: That does not print any duplicate numbers
# SortbyAbsoluteValues: That takes the absolute values of all transmitted numbers before 
# If a keyword argument is passed that is not one of the three above Print "Error: Not a valid Paramater" and return nothing 
# The function should return the sorted list
import math

def sortedTheseNumbers(*args, **kwargs):
    # Default kwargs to False
    reverse = False
    noDuplicates = False
    absolute = False
    # STore kwargs in variables
    for keys, value in kwargs.items():
        if keys == 'Reverse':
            reverse = value
        elif keys == 'NoDuplicates':
            noDuplicates = value
        elif keys == 'SortbyAbsoluteValues':
            absolute = value
        # If unrecognized kwarg, print error and return
        elif keys != 'Reverse' and keys != 'SortbyAbsoluteValues' and keys != 'NoDuplicates':
            print("Error: Not a valid Parameter")
            return

    # Create list from args
    listNum = [item for item in args]

    # Sort initially
    listNum = sorted(listNum)
    #Contains arguments to be passed to sorted function
    sortArgs = {}

    #Convert list to set and back to list gets rid of duplicates
    if noDuplicates:
        listNum = list(set(listNum))

    #Establish arguments for sorted function
    if reverse:
        sortArgs['reverse'] = True
    if absolute:
        sortArgs['key'] = abs

    #Call sorted function with new arguments
    listNum = sorted(listNum, **sortArgs)

    return listNum


# Problem 2
# A class that represents a point in space
# required variables and methods
# x - stores the x value of the point
# y - stores the y value of the point
# z - stores the z value of the point
# __init__  (method) - Should take in x, y, and z parameters and set their values
# __str__ (method) - Should return a string representation of the point. It should be formatted like a tuple ex: (x, y, z)
# __eq__ (method) - Should take in a Point object and return true if the x, y and z values of the input point are the same as the x, y, and z values of the calling point

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return

    def __str__(self):
        stringXYZ = (self.x, self.y, self.z)
        return str(stringXYZ)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y and self.z == p.z

# This class holds a list of 3D points which it uses to construct the bounding box
# required variables and methods
# points - stores the list of Point objects
# __init__ (method) - Should take in a list of Point objects and set the value of points
# add (method) - takes a Point object as input and inserts it in to the points list
# remove (method)- takes a Point object as input and removes it from Points list. Should do nothing if point is not in list
class PointCloudData:
    def __init__(self, Points):
        self.points = []
        for i in range(len(Points)):
            a = Points[i]
            self.points.append(Point(a.x, a.y, a.z))
        return

    def add(self, p):
        self.points.append(Point(p.x, p.y, p.z))
        return

    def remove(self, p):
        self.points.remove(Point(p.x, p.y, p.z))
        return

# This class represents a bounding box. It stores the center and dimensions of the box. This class is a subclass of PointCloudData
# center (variable) - A Point object used to store the location of the box in Cartesian space. The point should be at the center of the box.
# dimensions (variable) - A list with the width, height, and depth of the bounding box.
# __init__ (method) - Should take in a list of points as input and then call the superclass’s init method. It should then calculate and set the center and dimensions of the box.
# updateBox (method) - This method should take in a new list of points for the bounding box and should update the dimensions and center.
# collisionCheck (method) - this method takes in a BoundingBox, b, as an input and checks to see if the passed bounding box b is in collision with it and returns true if so and otherwise false.
# __add__ (method) - This method should take in a BoundingBox, b, as an input and it should combine the two bounding boxes. It should return a bounding box that minimally contains both bounding boxes. Note: this method overrides the + operation. This means that if you say BoundingBox1 + BoundingBox2, what is really happening is you are saying BoundingBox1.__add__(BoundingBox2).
# __len__ (method) - This method should return the volume of the bounding box

class BoundingBox(PointCloudData):
    def __init__(self, Points):
        super().__init__(Points)
        centerX = (self.points[0].x + self.points[1].x) / 2
        width = abs(self.points[0].x - self.points[1].x)
        centerY = (self.points[0].y + self.points[1].y) / 2
        length = abs(self.points[0].y - self.points[1].y)
        centerZ = (self.points[0].z + self.points[1].z) / 2
        height = abs(self.points[0].z - self.points[1].z)
        self.center = Point(centerX, centerY, centerZ)
        self.dimensions = [width, length, height]
        return

    def updateBox(self, Points):
        self.points[0].x = Points[2].x
        self.points[0].y = Points[2].y
        self.points[0].z = Points[2].z
        self.__init__(Points)
        return

    def collisionCheck(self, b):
        if self.points[0].x < self.points[1].x:
            a_minX = self.points[0].x
            a_maxX = self.points[1].x
        else:
            a_minX = self.points[1].x
            a_maxX = self.points[0].x

        if b.points[0].x < b.points[1].x:
            b_minX = b.points[0].x
            b_maxX = b.points[1].x
        else:
            b_minX = b.points[1].x
            b_maxX = b.points[0].x


        if self.points[0].y < self.points[1].y:
            a_minY = self.points[0].y
            a_maxY = self.points[1].y
        else:
            a_minY = self.points[1].y
            a_maxY = self.points[0].y

        if b.points[0].y < b.points[1].y:
            b_minY = b.points[0].y
            b_maxY = b.points[1].y
        else:
            b_minY = b.points[1].y
            b_maxY = b.points[0].y


        if self.points[0].z < self.points[1].z:
            a_minZ = self.points[0].z
            a_maxZ = self.points[1].z
        else:
            a_minZ = self.points[1].z
            a_maxZ = self.points[0].z

        if b.points[0].z < b.points[1].z:
            b_minZ = b.points[0].z
            b_maxZ = b.points[1].z
        else:
            b_minZ = b.points[1].z
            b_maxZ = b.points[0].z

        return (a_minX <= b_maxX and a_maxX >= b_minX) and (a_minY <= b_maxY and a_maxY >= b_minY) and (a_minZ <= b_maxZ and a_maxZ >= b_minZ)

    def __add__(self, b):
        if self.points[0].x < self.points[1].x:
            a_minX = self.points[0].x
            a_maxX = self.points[1].x
        else:
            a_minX = self.points[1].x
            a_maxX = self.points[0].x

        if b.points[0].x < b.points[1].x:
            b_minX = b.points[0].x
            b_maxX = b.points[1].x
        else:
            b_minX = b.points[1].x
            b_maxX = b.points[0].x


        if self.points[0].y < self.points[1].y:
            a_minY = self.points[0].y
            a_maxY = self.points[1].y
        else:
            a_minY = self.points[1].y
            a_maxY = self.points[0].y

        if b.points[0].y < b.points[1].y:
            b_minY = b.points[0].y
            b_maxY = b.points[1].y
        else:
            b_minY = b.points[1].y
            b_maxY = b.points[0].y


        if self.points[0].z < self.points[1].z:
            a_minZ = self.points[0].z
            a_maxZ = self.points[1].z
        else:
            a_minZ = self.points[1].z
            a_maxZ = self.points[0].z

        if b.points[0].z < b.points[1].z:
            b_minZ = b.points[0].z
            b_maxZ = b.points[1].z
        else:
            b_minZ = b.points[1].z
            b_maxZ = b.points[0].z

        lhw = b_maxX - a_minX
        centerNum = b_minX - a_minY


        b.center = Point(centerNum, centerNum, centerNum)
        b.dimensions = [lhw, lhw, lhw]

        bb3 = b

        return bb3

    def __len__(self):
        return self.dimensions[0] * self.dimensions[1] * self.dimensions[2]


#You can test your code by running testcases.py
