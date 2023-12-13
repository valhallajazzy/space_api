import os
import random
from time import sleep

import telegram
from telegram import InputMediaPhoto
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token=f'{os.environ["TELEGRAM_TOKEN"]}')
    images = [i[2] for i in os.walk('./images/')][0]
    while True:
        random.shuffle(images)
        for image in images:
            media = InputMediaPhoto(media=open(f'./images/{image}', 'rb'))
            bot.send_media_group(chat_id='@spaceimg_channel', media=[media])
            sleep(os.getenv("DRINKS_PATH", default=14400))


if __name__ == '__main__':
    main()