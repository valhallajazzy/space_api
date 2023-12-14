from pathlib import Path
import argparse

import requests


def fetch_spacex_last_launch(launch_id='latest'):
    Path("./images").mkdir(parents=True, exist_ok=True)
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]

    for link_number, link in enumerate(images):
        response = requests.get(link)
        response.raise_for_status()
        with open(f"./images/spacex_{link_number}.jpg", 'wb') as file:
            file.write(response.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--launch", help='Введите id запуска')
    args = parser.parse_args()
    if args.launch_id != None:
        fetch_spacex_last_launch(args.launch_id)
    else:
        fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
