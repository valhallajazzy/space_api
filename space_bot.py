import telegram
from telegram import InputMediaPhoto
import os
from dotenv import load_dotenv

load_dotenv()

bot = telegram.Bot(token=f'{os.environ["TELEGRAM_TOKEN"]}')
updates = bot.get_updates()

print(bot.get_me())
bot.send_message(chat_id='@spaceimg_channel', text='Привет, как дела?')
media_1 = InputMediaPhoto(media=open('./images/earth_1.png', 'rb'))
bot.send_media_group(chat_id='@spaceimg_channel', media=[media_1])
