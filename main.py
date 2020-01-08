from shapely.geometry import Point, LineString, Polygon
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import descartes


def lesson_one():

    print('\n' + "Lesson One:" + '\n')
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

    print("x co-ords in set " + str(np.array(line_df['x'].tolist())))
    print("y co-ords in set " + str(np.array(line_df['y'].tolist())))

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

    print('\n' + "Polygons" + '\n')

    # Create a Polygon from the coordinates
    poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

    # We can also use our previously created Point objects (same outcome)
    # --> notice that Polygon object requires x,y coordinates as input
    poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])

    # Geometry type can be accessed as a String
    poly_type = poly.geom_type

    # Using the Python's type function gives the type in a different format
    poly_type2 = type(poly)

    # Let's see how our Polygon looks like
    print(poly)
    print(poly2)
    print("Geometry type as text:", poly_type)
    print("Geometry how Python shows it:", poly_type2)

    """
    Notice that Polygon has double parentheses around the coordinates. 
    This is because Polygon can also have holes inside of it. As the help of Polygon -object tells,
    a Polygon can be constructed using exterior coordinates and interior coordinates (optional) where
    the interior coordinates creates a hole inside the Polygon:
    """

    print('\n' + "Creating a polygon with a hole inside" +'\n')

    # Let's create a bounding box of the world and make a whole in it
    # First we define our exterior
    world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

    # Let's create a single big hole where we leave ten decimal degrees at the boundaries of the world
    # Notice: there could be multiple holes, thus we need to provide a list of holes
    hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

    # World without a hole
    world = Polygon(shell=world_exterior)

    # Now we can construct our Polygon with the hole inside
    world_has_a_hole = Polygon(shell=world_exterior, holes=hole)

    print("world =  " + str(world))
    print("world with hole = " + str(world_has_a_hole))
    print('\n' + "Polygon attributes and functions" + '\n')
    print(".centroid, .area, .bounds, .exterior, .exterior.length" + '\n')
    print("MultiPoint and MultiLineString objects also exist with special attributes and functions")


def lesson_two():

    fp = "C:/Users/danie/Documents/GitHub/helsinki_gis_course/Resources/2_Data/DAMSELFISH_distributions_SELECTIONS.shp"
    data = gpd.read_file(fp)

    #data.plot()
    #plt.show()
    data['geometry'].head()
    # Writing to a shape file

    # Create a output path for the data
    out = "C:/Users/danie/Documents/GitHub/helsinki_gis_course/Resources/2_Data/DAMSELFISH_distributions_SELECTIONS.shp"

    # Select first 50 rows
    selection = gpd.GeoDataFrame(data[0:5])

    for index, row in selection.iterrows():
        poly_area = row['geometry'].area
        print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))

    selection['area'] = selection.area
    print(selection['area'].head(2))
    # Write those rows into a new Shapefile (the default output file format is Shapefile)

    # selection.to_file(out)


    # Maximum area
    max_area = selection['area'].max()

    # Mean area
    mean_area = selection['area'].mean()

    print("Max area: %s\nMean area: %s" % (round(max_area, 2), round(mean_area, 2)))

    # Creating geometries into a GeoDataFrame
    newdata = gpd.GeoDataFrame()

    print("gpd.GeoDataFrame() yields " + str(newdata))

    newdata['geometry'] = None

    coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104),
                           (24.950958, 60.169990)]

    # Create a Shapely polygon from the coordinate-tuple list
    poly = Polygon(coordinates)
    newdata.loc[0, 'geometry'] = poly
    newdata.loc[0, 'Location'] = 'Senaatintori'

    # Set the coordinate reference system to WGS84
    from fiona.crs import from_epsg
    newdata.crs = from_epsg(4326)

    out_fp = "C:/Users/danie/Documents/GitHub/helsinki_gis_course/Resources/2_Data/helsinki_senate.shp"
    newdata.to_file(out_fp)
    #print(newdata)

    # .tocrs() to change the projection


def lesson_three():

    # Geocoding addresses to points
    # Retrieve OS Map data
    # Data classifications

    # Geopy does the geocoding through thrid party geocoders, we will use Nominatim


    pass


if __name__ == "__main__":
    #lesson_one()
    lesson_two()