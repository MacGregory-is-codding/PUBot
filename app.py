import telebot

import config
from commands import *

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.from_user.id == config.ADMIN_ID: 
        # /screen
        if message.text == '/screen':
            screen(bot, message)
            return
        
        # /shutdown
        if message.text == '/shutdown':
            shutdown(bot, message)
            return 


bot.polling(none_stop=True, interval=0)
