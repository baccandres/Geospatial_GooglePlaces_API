# GeoSpatial

This project is about choosing the best city out of Madrid, Trentino-Alto Adige and Vancouver to establish a new company based on the least sum of meters between the nearest airport, nearest school and nearest bar amongst those cities.

In order to achieve that, the project is divided in 5 parts:

1) Establishing the coordinates for each city
2) Calling the Google Places API to find the airports, schools and bars within a radio
3) Inserting API requests into mongoDB
4) Employ mongoDB from Python to calculate the distances between airports, schools and bars and the coordinates established in part 1.
5) Choose the city with the smallest aggregated of meters between the three categories and create a map to display them all

Open 'notebooks/Maps and Conclusions' to find out the winning city, its map and locations.

notebooks:
-api and collections
-Maps and Conclusions

src:
-cleaning: containing the functions used to clean and set up the file

Python libraries: pymongo, folium, sys, pandas, googlemaps, os, requests, json, geopandas, cartoframes, dotenv, shapely

References:
1) https://towardsdatascience.com/generating-geocodes-using-google-maps-api-eb56028821a6
2) https://developers.google.com/maps/documentation/places/web-service/search-nearby
3) https://developers.google.com/maps/documentation/places/web-service/supported_types
