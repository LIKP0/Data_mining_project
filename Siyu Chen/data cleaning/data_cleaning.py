import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from shapely import geometry
import geopandas
from shapely.geometry import Point, Polygon

# Gaode API, not used here
key = 'fc77699198d4e84ffb8f244052972253'

# read shenzhen boundary
boundary = geopandas.read_file('../material/440300.json')
boundary_exploded = boundary.explode()

# def valid longtitude,latitude method
def isValidPos(lon,lat):
    p = Point(lon,lat)
    for i in range(5):
        if(p.within(boundary_exploded['geometry'][0][i])):
            return True
    return False

# filter data
df = pd.read_csv('../material/taxi2.csv')
df['isValid'] = df.apply(lambda x:isValidPos(x.lon,x.lat),axis=1)
df = df.drop(df[~df['isValid']].index)
# save to csv file
df = df.iloc[:,:-1]
df.to_csv('../material/taxi_clean.csv')
# prompt message
print("complete")