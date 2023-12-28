import os
import random
import argparse
from pathlib import Path
from time import sleep
from utils import send_photo

import telegram
from telegram.error import NetworkError
from dotenv import load_dotenv


def send_photo_to_channel(token, telegram_chat_id, time_interval, image_path, config_path):
    bot = telegram.Bot(token=token)
    if image_path:
        send_photo(bot, image_path, telegram_chat_id)
    else:
        images = [image[2] for image in os.walk(config_path)][0]
        while True:
            try:
                telegram.Bot(token=token)
                random.shuffle(images)
                for image in images:
                    send_photo(bot, Path(config_path) / f'{image}', telegram_chat_id)
                    sleep(int(time_interval))
            except NetworkError as e:
                telegram.Bot(token=token)
                sleep(10)


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    time_interval = os.getenv("TIME_INTERVAL", default=14400)
    path_to_folder_with_images=os.getenv("PATH_TO_FOLDER", default=Path.cwd() / 'images')
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help='Введите путь до картинки, которую хотите отправить',
                        default=None)
    args = parser.parse_args()
    send_photo_to_channel(token, telegram_chat_id, time_interval, args.path, path_to_folder_with_images)


if __name__ == '__main__':
    main()