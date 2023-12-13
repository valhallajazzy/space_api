import telegram


bot = telegram.Bot(token='6459044861:AAFn3qiOGL6U8AImQ4tXpWRWP6bfeq84XmE')
updates = bot.get_updates()

print(bot.get_me())
bot.send_message(chat_id='@spaceimg_channel', text='Привет, как дела?')
