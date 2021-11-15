import pandas as pd
import googlemaps
import os
import pymongo
import requests
import json
import geopandas as gpd
from pymongo import MongoClient
from cartoframes.viz import Map, Layer, popup_element
from dotenv import load_dotenv


load_dotenv()
g_API = os.getenv('key')
gmaps_key = googlemaps.Client(key=g_API)

def geocode (x):
    """
    function to get location
    coordinates [lat, lng] from 
    an address.
    """
    data = requests.get(f"https://geocode.xyz/{x}?json=1").json()
    try:
        return {"type": "Point", "coordinates": [data["latt"], data["longt"]]}
    except:
        return data

def lngt (geometry):
    """
    get lattitude from google places API json

    """
    return geometry['location']['lng']

def latt (geometry):
    """
    get longitude from google places API json

    """
    return geometry['location']['lat']

def typePoint (lng, lat):
    """
    get type point format for intersections in pandas
    
    """
    return {'type': 'Point', 'coordinates': [lng, lat]}

def nearby (lat, lng, radius, keyword):
    """
    lat = lattitude of the address
    lng = longitude of the address
    radius = in mts
    keyword = to define the type of place to be searched
    
    returns Google Places API in a dataframe containing 
    all columns needed for geoqueries in MongoDB.
    
    """
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={g_API}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    df_x = pd.DataFrame(response.json()['results'])
    df_x['types'] = df_x.types[0][0]
    df_x['longitude'] = df_x.geometry.apply(lngt)
    df_x['lattitude'] = df_x.geometry.apply(latt)
    df_x['intersect'] = df_x.apply(lambda x: typePoint(x['longitude'], x['lattitude']), axis = 1)
    df_x = df_x[['types', 'name', 'longitude', 'lattitude']]
    
    return df_x

