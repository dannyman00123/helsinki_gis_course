from shapely.geometry import Point, LineString, Polygon
import pandas as pd
import numpy as np


def create_point_geom(x, y):

    point = Point(x, y)

    return point


def create_line_geom(points):

    line = LineString(points)

    return line


def create_poly_geom(points):

    polygon = Polygon([[p.x, p.y] for p in points])

    return polygon


# Functions
point1 = create_point_geom(1, 1)
point2 = create_point_geom(2, 2)
point3 = create_point_geom(3, 3)

line1 = create_line_geom([point1, point2, point3])
point_array = [point1, point2, point3]
polygon1 = create_poly_geom(point_array)

print(str(line1))
print(str(polygon1))
