from urllib.parse import urlsplit, unquote
import os
from os.path import splitext
from pathlib import Path

import requests
from telegram import InputMediaPhoto
from dotenv import load_dotenv


def create_image(image_link, image_number, word_prefix, params=None):
    response = requests.get(image_link, params=params)
    response.raise_for_status()
    url_path = unquote(urlsplit(image_link).path)
    file_extension = splitext(url_path)[1]
    outpath = Path.cwd() / 'images' / f'{word_prefix}_{image_number}{file_extension}'
    with open(outpath, 'wb') as file:
        file.write(response.content)


def send_photo(bot, image_path):
    load_dotenv()
    with open(image_path, 'rb') as im:
        bot.send_media_group(chat_id=os.environ['TELEGRAM_CHAT_ID'], media=[InputMediaPhoto(im)])