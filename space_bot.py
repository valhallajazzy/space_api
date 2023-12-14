import os
import random
import argparse
from time import sleep

import telegram
from telegram import InputMediaPhoto
from dotenv import load_dotenv


def send_photo_to_channel(token, time_interval, image_path=None):
    bot = telegram.Bot(token=token)
    if image_path != None:
        media = InputMediaPhoto(media=open(image_path, 'rb'))
        bot.send_media_group(chat_id='@spaceimg_channel', media=[media])
    else:
        images = [i[2] for i in os.walk('./images/')][0]
        while True:
            random.shuffle(images)
            for image in images:
                media = InputMediaPhoto(media=open(f'./images/{image}', 'rb'))
                bot.send_media_group(chat_id='@spaceimg_channel', media=[media])
                sleep(int(time_interval))


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    time_interval = os.getenv("TIME_INTERVAL", default=14400)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help='Введите путь до картинки, которую хотите отправить')
    args = parser.parse_args()
    if args.path != None:
        send_photo_to_channel(token, time_interval, args.path)
    else:
        send_photo_to_channel(token, time_interval)


if __name__ == '__main__':
    main()