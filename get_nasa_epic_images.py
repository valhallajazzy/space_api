import os
from datetime import datetime
from pathlib import Path
from utils import download_image

import requests
from dotenv import load_dotenv


def get_nasa_epic_images(token, path_to_folder_with_images):
    path_to_folder_with_images.mkdir(parents=True, exist_ok=True)
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    images = response.json()

    for image_number, data in enumerate(images):
        image_time = datetime.strptime(data["date"], '%Y-%m-%d %H:%M:%S').date()
        image_name = data["image"]
        payload = {"api_key": token}
        url = f'https://api.nasa.gov/EPIC/archive/natural/{image_time.year}' \
              f'/{image_time.month}/{image_time.day}/png/{image_name}.png'
        download_image(url, image_number, 'earth', path_to_folder_with_images, payload)


def main():
    path_to_folder_with_images = os.getenv("PATH_TO_FOLDER", default=Path.cwd() / 'images')
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    get_nasa_epic_images(token, path_to_folder_with_images)


if __name__ == '__main__':
    main()
