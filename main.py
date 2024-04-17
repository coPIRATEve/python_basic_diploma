import telebot
from config_data import config
from comands_settings import start, help_command, website, menu, min_temp, max_temp, get_weather, get_coord, history, send_history
from telegram import Update
from telegram.ext import CallbackContext


count = 1

# Создание объекта бота
bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN)
api = config.API_KEY
HISTORY = 'history.txt'

# Обработчики команд
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

@bot_prikol.message_handler(commands=['low'])
def low_handler(message):
    min_temp(bot_prikol, message)

@bot_prikol.message_handler(commands=['high'])
def high_handler(message):
    max_temp(bot_prikol, message)

@bot_prikol.message_handler(commands=['weather'])
def weather_handler(message):
    get_weather(bot_prikol, message)

@bot_prikol.message_handler(commands=['coords'])
def coords_handler(message):
    get_coord(bot_prikol, message)

# Обработчик текстовых сообщений

@bot_prikol.message_handler(commands=['history'])
def history(update: Update, context: CallbackContext) -> None:
    history(update, context)  # Используем функцию history из модуля default

@bot_prikol.message_handler(content_types=['text'])
def send_history(message):
    send_history(message)  # Используем функцию send_history из модуля default

# Запуск бота
if __name__ == "__main__":
    bot_prikol.polling()