import telebot
from config_data import config
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()
bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN, state_storage=storage)

@bot_prikol.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, я бот-синоптик '
    else:
        mess = f'Привет, <b>{message.from_user.first_name}</b>, я бот-синоптик '
    bot_prikol.send_message(message.chat.id, mess, parse_mode='html')