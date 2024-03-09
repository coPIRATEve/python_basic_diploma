import telebot
import json
import requests
from telebot import types
from config_data import config
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()

bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN, state_storage=storage)
api = config.API_KEY

@bot_prikol.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, я бот-синоптик '
    else:
        mess = f'Привет, <b>{message.from_user.first_name}</b>, я бот-синоптик '
    bot_prikol.send_message(message.chat.id, mess, parse_mode='html')

@bot_prikol.message_handler(commands=["help"])
def help_command(message):
    markup = types.InlineKeyboardMarkup()
    bot_prikol.send_message(message.chat.id, 'Этот бот создан для получения фактов о погоде', reply_markup=markup)

@bot_prikol.message_handler(commands=['web'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Погода", url="https://www.accuweather.com/ru/world-weather"))
    bot_prikol.send_message(message.chat.id, 'Проверь прогноз!', reply_markup=markup)

@bot_prikol.message_handler(commands=['menu'])
def menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    low_button = telebot.types.KeyboardButton('/low')
    high_button = telebot.types.KeyboardButton('/high')
    coords_button = telebot.types.KeyboardButton('/coords')
    weather_button = telebot.types.KeyboardButton('/weather')
    markup.add(low_button, high_button, coords_button, weather_button)
    bot_prikol.reply_to(message, "Выберите действие:", reply_markup=markup)

# Обработчик команды /low
@bot_prikol.message_handler(commands=['low'])
def min_temp(message):
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, process_min_temp)

def process_min_temp(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Минимальная температура: {data["main"]["temp_min"]}')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')

@bot_prikol.message_handler(commands=['high'])
def max_temp(message):
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, process_max_temp)

def process_max_temp(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Максимальная температура: {data["main"]["temp_max"]}')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')

@bot_prikol.message_handler(commands=['weather'])
def get_weather(message):
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, process_weather)

def process_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Текущая температура: {data["main"]["temp"]}°C')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')

# Обработчик команды /coords
@bot_prikol.message_handler(commands=['coords'])
def get_coord(message):
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, process_coords)

def process_coords(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Широта: {data["coord"]["lat"]}, Долгота: {data["coord"]["lon"]}')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')


bot_prikol.polling(none_stop=True)
