from datetime import datetime
import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote
from os.path import splitext


def fetch_spacex_last_launch(url, path):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]

    for link_number, link in enumerate(images):
        response = requests.get(link)
        response.raise_for_status()
        with open(f"{path}/spacex_{link_number}.jpg", 'wb') as file:
            file.write(response.content)


def nasa_apod():
    Path("./images").mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {"api_key": "QpxEWeq1I46dI2BUhUNQ3ouFMrkU5dc5eJXRAiBv",
               "count": 20,
               "thumbs": False,
               }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for image_number, data in enumerate(images):
        image_link = data["url"]
        payload = {"api_key": "QpxEWeq1I46dI2BUhUNQ3ouFMrkU5dc5eJXRAiBv"}
        response = requests.get(image_link, params=payload)
        response.raise_for_status()
        url_path = unquote(urlsplit(image_link).path)
        file_extension = splitext(url_path)[1]

        with open(f"./images/nasa_apod_{image_number}{file_extension}", 'wb') as file:
            file.write(response.content)


def epic():
    Path("./images").mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {"api_key": "QpxEWeq1I46dI2BUhUNQ3ouFMrkU5dc5eJXRAiBv"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for image_number, data in enumerate(images):
        image_time = datetime.strptime(data["date"], '%Y-%m-%d %H:%M:%S').date()
        image_name = data["image"]
        payload = {"api_key": "QpxEWeq1I46dI2BUhUNQ3ouFMrkU5dc5eJXRAiBv"}
        url = f'https://api.nasa.gov/EPIC/archive/natural/{image_time.year}/{image_time.month}/{image_time.day}/png/{image_name}.png'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        with open(f"./images/earth_{image_number}.png", 'wb') as file:
            file.write(response.content)


epic()