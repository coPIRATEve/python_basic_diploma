import telebot
from config_data import config
from telebot.storage import StateMemoryStorage
from comands_settings import start, help_command, website, menu,history_handler, min_temp, max_temp, get_weather, get_coord
from database.utils.outbase import outbaseInterface
storage = StateMemoryStorage()

bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN, state_storage=storage)
api = config.API_KEY

bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN)

outbase = outbaseInterface()

@bot_prikol.message_handler(commands=['history'])
def history_command_handler(message):
    history_handler(bot_prikol, outbase, message)

@bot_prikol.message_handler(commands=['start'])
def start_handler(message):
    start(message)

@bot_prikol.message_handler(commands=["help"])
def help_command_handler(message):
    help_command(message)

@bot_prikol.message_handler(commands=['web'])
def website_handler(message):
    website(message)

@bot_prikol.message_handler(commands=['menu'])
def menu_handler(message):
    menu(message)

# Обработчик команды /low
@bot_prikol.message_handler(commands=['low'])
def low_handler(message):
    min_temp(bot_prikol, message, api)

@bot_prikol.message_handler(commands=['high'])
def high_handler(message):
    max_temp(bot_prikol, message, api)

@bot_prikol.message_handler(commands=['weather'])
def weather_handler(message):
    get_weather(bot_prikol, message, api)

@bot_prikol.message_handler(commands=['coords'])
def coords_handler(message):
    get_coord(bot_prikol, message, api)


bot_prikol.polling(none_stop=True)
