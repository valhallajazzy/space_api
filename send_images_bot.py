import os
import random
import argparse
from time import sleep
from utils import send_photo

import telegram
from dotenv import load_dotenv


def send_photo_to_channel(token, time_interval, image_path):
    bot = telegram.Bot(token=token)
    if image_path != None:
        send_photo(bot, image_path)
    else:
        images = [i[2] for i in os.walk('./images/')][0]
        while True:
            random.shuffle(images)
            for image in images:
                send_photo(bot, f'./images/{image}')
                sleep(int(time_interval))


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    time_interval = os.getenv("TIME_INTERVAL", default=14400)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help='Введите путь до картинки, которую хотите отправить',
                        default=None)
    args = parser.parse_args()
    send_photo_to_channel(token, time_interval, args.path)



if __name__ == '__main__':
    main()