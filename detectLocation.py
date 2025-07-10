import requests
from dotenv import load_dotenv
load_dotenv()
import os
import datetime
import time
class Location:
    def locationCoordinates():
        try:
            response = requests.get(os.getenv('url'))
            data=response.json()
            #print(data)
            loc = data['loc'].split()
            #print("Loc=",loc)
            lat,long=float(loc[0].split(',')[0]), float(loc[0].split(",")[1])
            city = data.get('city', 'Unknown')
            state = data.get('region', 'Unknown')
            return lat, long, city, state
        except Exception as error:
            print(error)