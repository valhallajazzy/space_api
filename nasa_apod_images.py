from pathlib import Path
from urllib.parse import urlsplit, unquote
import os
from os.path import splitext
import argparse

import requests
from dotenv import load_dotenv


def nasa_apod_images(token, images_count=20):
    Path("./images").mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {"api_key": token,
               "count": images_count,
               "thumbs": False,
               }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for image_number, data in enumerate(images):
        image_link = data["url"]
        payload = {"api_key": token}
        response = requests.get(image_link, params=payload)
        response.raise_for_status()
        url_path = unquote(urlsplit(image_link).path)
        file_extension = splitext(url_path)[1]

        with open(f"./images/nasa_apod_{image_number}{file_extension}", 'wb') as file:
            file.write(response.content)


def main():
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", help='Введите требуемое количество фотографий', type=int)
    args = parser.parse_args()
    if args.count != None:
        nasa_apod_images(token, args.count)
    else:
        nasa_apod_images(token)


if __name__ == '__main__':
    main()
