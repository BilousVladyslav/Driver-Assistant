import os
import time
import random
import logging

import requests
from perlin_noise import PerlinNoise


CENTER_LATITUDE = 50.005992
CENTER_LONGITUDE = 36.229698

MAX_DISTANCE = 0.3037540341855561265

CAR_ID = os.environ.get('CAR_ID')
API_URL = os.environ.get('API_URL')
RUN = int(os.environ.get('RUN'))

octaves = 32
noise = PerlinNoise(octaves=octaves, seed=1)
lat = CENTER_LATITUDE
long = CENTER_LONGITUDE
mult_lat = random.random()
mult_long = random.random()


def update_coordinates(latitude, longitude):
    url = f'{API_URL}{CAR_ID}/'
    data = {
        "latitude": latitude,
        "longitude": longitude
    }
    try:
        requests.put(url, json=data)
    except Exception as e:
        logging.error(str(e))


while RUN:
    mult_lat = noise([mult_lat])
    mult_long = noise([mult_long])
    lat = CENTER_LATITUDE + MAX_DISTANCE * mult_lat
    long = CENTER_LONGITUDE + MAX_DISTANCE * mult_long

    update_coordinates(lat, long)
    time.sleep(1)
