import requests
import json
from config_data import config

api = config.API_KEY

def min_temp(bot_prikol, message):
    """
    Обработчик команды /low. Выводит минимальную температуру для указанного города.

    Args:
        bot_prikol: Объект бота TeleBot.
        message: Объект сообщения от пользователя.
    """
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, lambda msg: process_min_temp(msg, bot_prikol, api))

def process_min_temp(message, bot_prikol, api):
    """
    Обрабатывает полученный город и выводит минимальную температуру.

    Args:
        message: Объект сообщения от пользователя.
        bot_prikol: Объект бота TeleBot.
        api: Ключ API для доступа к сервису погоды.
    """
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Минимальная температура: {data["main"]["temp_min"]}')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')

def max_temp(bot_prikol, message):
    """
    Обработчик команды /high. Выводит максимальную температуру для указанного города.

    Args:
        bot_prikol: Объект бота TeleBot.
        message: Объект сообщения от пользователя.
    """
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, lambda msg: process_max_temp(msg, bot_prikol, api))

def process_max_temp(message, bot_prikol, api):
    """
    Обрабатывает полученный город и выводит максимальную температуру.

    Args:
        message: Объект сообщения от пользователя.
        bot_prikol: Объект бота TeleBot.
        api: Ключ API для доступа к сервису погоды.
    """
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Максимальная температура: {data["main"]["temp_max"]}')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')

def get_weather(bot_prikol, message):
    """
    Обработчик команды /weather. Выводит текущую температуру для указанного города.

    Args:
        bot_prikol: Объект бота TeleBot.
        message: Объект сообщения от пользователя.
    """
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, lambda msg: process_weather(msg, bot_prikol, api))

def process_weather(message, bot_prikol, api):
    """
    Обрабатывает полученный город и выводит текущую температуру.

    Args:
        message: Объект сообщения от пользователя.
        bot_prikol: Объект бота TeleBot.
        api: Ключ API для доступа к сервису погоды.
    """
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Текущая температура: {data["main"]["temp"]}°C')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')

def get_coord(bot_prikol, message):
    """
    Обработчик команды /coords. Выводит координаты указанного города.

    Args:
        bot_prikol: Объект бота TeleBot.
        message: Объект сообщения от пользователя.
    """
    bot_prikol.reply_to(message, "Введите название города:")
    bot_prikol.register_next_step_handler(message, lambda msg: process_coords(msg, bot_prikol, api))

def process_coords(message, bot_prikol, api):
    """
    Обрабатывает полученный город и выводит его координаты.

    Args:
        message: Объект сообщения от пользователя.
        bot_prikol: Объект бота TeleBot.
        api: Ключ API для доступа к сервису погоды.
    """
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot_prikol.reply_to(message, f'Широта: {data["coord"]["lat"]}, Долгота: {data["coord"]["lon"]}')
    else:
        bot_prikol.reply_to(message, f'Город указан неверно.')
