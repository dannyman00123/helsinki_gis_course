from shapely.geometry import Point, LineString, Polygon
import pandas as pd
import numpy as np
import create_geometries as cg
import read_attributes as ra


def create_dataframe():
    df = pd.read_csv("C:/Users/danie/Documents/GitHub/helsinki_gis_course/Resources/travelTimes_2015_Helsinki.txt", sep=';')
    cols = ['from_x', 'from_y', 'to_x', 'to_y', 'total_route_time']
    df = df[cols]
    return df

def create_point_geom_tuple(tuple):

    point = Point(tuple[0], tuple[1])

    return point

df = create_dataframe()

# take from x and from y and add new column of Point objects (orig_points)
#df['orig_points'] = list(zip(df.from_x, df.from_y))
df['orig_points'] = df[['from_x', 'from_y']].apply(create_point_geom_tuple, axis=1)
#df['orig_points'] = df['orig_points'].apply(Point, axis=1)
# take to x and to y and add new column of Point objects (dest_points)
#df['dest_points'] = list(zip(df.to_x, df.to_y))
df['dest_points'] = df[['to_x', 'to_y']].apply(create_point_geom_tuple, axis=1)
#df['dest_points'] = df['dest_points'].apply(Point, axis=1)

print("Done")
