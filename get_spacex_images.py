import os
from pathlib import Path
import argparse
from utils import download_image

import requests


def fetch_spacex_last_launch(launch_id, path_to_folder_with_images):
    path_to_folder_with_images.mkdir(parents=True, exist_ok=True)
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]

    for link_number, link in enumerate(images):
        download_image(link, link_number, 'spacex', path_to_folder_with_images)


def main():
    path_to_folder_with_images = os.getenv("PATH_TO_FOLDER", default=Path.cwd() / 'images')
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--launch", help='Введите id запуска', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch, path_to_folder_with_images)


if __name__ == '__main__':
    main()
