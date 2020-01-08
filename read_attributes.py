from shapely.geometry import Point, LineString, Polygon
import pandas as pd
import numpy as np
import create_geometries as cg

"""
Write your codes into a single read_attributes.py -file and upload the script to your personal GitHub
Exercise-1 repository.

Create a function called getCentroid() that takes any kind of Shapely's geometric -object as input and
returns a centroid of that geometry. Demonstrate the usage of the function.

Create a function called getArea() that takes a Shapely's Polygon -object as input and returns the area
of that geometry. Demonstrate the usage of the function.

Create a function called getLength() takes either a Shapely's LineString or Polygon -object as input.
Function should check the type of the input and returns the length of the line if input is LineString
and length of the exterior ring if input is Polygon. If something else is passed to the function,
it should tell the user --> "Error: LineString or Polygon geometries required!".
Demonstrate the usage of the function.
"""


def getCentroid(geometric_object):
    return str(geometric_object.centroid)


def getArea(polygon):
    return str(polygon.area)


def getLength(geometric_obj):

    try:
        if str(geometric_obj.type) == "LineString":
            return geometric_obj.length
        elif str(geometric_obj.type) == "Polygon":
            return geometric_obj.exterior.length
        else:
            print("Error: LineString or Polygon geometries required!")
    except TypeError as e:
        print(e)




point1 = cg.create_point_geom(1, 1)
point2 = cg.create_point_geom(2, 2)
point3 = cg.create_point_geom(3, 3)

point_array = [point1, point2, point3]

polygon1 = cg.create_poly_geom(point_array)
line1 = cg.create_line_geom([point1, point2, point3])

centroid1 = getCentroid(polygon1)
centroid2 = getCentroid(line1)
centroid3 = getCentroid(LineString([point1, point2]))

print(centroid1)
print(centroid2)
print(centroid3)

area1 = getArea(polygon1)
print(area1)

length1 = getLength(line1)
print("line length " + str(length1))
length2 = getLength(polygon1)
print("Polygon length " + str(length2))

length3 = getLength(point1)
