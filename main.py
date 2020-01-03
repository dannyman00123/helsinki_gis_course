import shapely
from shapely.geometry import Point, LineString, Polygon
import pandas as pd
import numpy as np

def lesson_one():

    point1 = Point(2.2, 4.2)
    point2 = Point(7.2, -25.1)
    point3 = Point(9.26, -2.456)

    #print(str(point1.x))
    print("point1.x  = {0:.2f}".format(point1.x))
    print("point2.coords  = " + str(point2.coords))
    print("point1.coords.xy = " + str(point1.coords.xy))

    point_dist = point1.distance(point2)

    # the returned distance is based on the projection of the points (degrees in WGS84, meters in UTM)
    print("point1.distance(point2) is {0:.2f} decimal degrees".format(point_dist))

    point3D = Point(9.26, -2.456, 0.57)
    point_type = type(point1)

    # LineString time
    line = LineString([point1, point2, point3])
    line_df = pd.DataFrame(np.array(line), columns=['x','y'])


    line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

    print("LineString line.xy yields " + str(line.xy))

    print("x coords in set " + str(np.array(line_df['x'].tolist())))
    print ("y coords in set " + str(np.array(line_df['y'].tolist())))

    print("Alternate way of accessing column data:")

    # Extract x coordinates
    line_x = line.xy[0]
    # Extract y coordinates straight from the LineObject by referring to a array at index 1
    line_y = line.xy[1]
    print(line_x)
    print(line_y)

    # specific attributes of LineString objects can also be found
    print(str(line.length))
    print(str(line.centroid))
    print(str(type(line.centroid)))

if __name__ == "__main__":
    lesson_one()