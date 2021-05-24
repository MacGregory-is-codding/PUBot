from io import BytesIO
from time import sleep

from pc_controller import *

# /screen
def screen(bot, message):
    image = get_screen()
    bio = BytesIO()
    bio.name = 'image.png'
    image.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(
        message.from_user.id,
        photo=bio,
        reply_to_message_id=message.id
    )    

# /shutdown
def shutdown(bot, message):
    pc_off()
    sleep(1)
    screen(bot, message)
    