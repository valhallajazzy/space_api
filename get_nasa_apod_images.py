from pathlib import Path
import os
import argparse
from utils import download_image

import requests
from dotenv import load_dotenv


def get_nasa_apod_images(token, images_count, path_to_folder_with_images):
    path_to_folder_with_images.mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {"api_key": token,
               "count": images_count,
               "thumbs": False,
               }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    media = response.json()

    for image_number, data in enumerate(media):
        if data['media_type'] == 'image':
            image_link = data["url"]
            payload = {"api_key": token}
            download_image(image_link, image_number, 'nasa_apod', path_to_folder_with_images, payload)


def main():
    path_to_folder_with_images=os.getenv("PATH_TO_FOLDER", default=Path.cwd() / 'images')
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", help='Введите требуемое количество фотографий', type=int,
                        default=20)
    args = parser.parse_args()
    get_nasa_apod_images(token, args.count, path_to_folder_with_images)


if __name__ == '__main__':
    main()
