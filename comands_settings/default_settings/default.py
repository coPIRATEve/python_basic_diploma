import telebot
from telebot import types
from config_data import config

bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN)

def start(message):
    """
    Обработчик команды /start. Приветствует пользователя.

    Args:
        message: Объект сообщения от пользователя.
    """
    if message.from_user.last_name:
        greeting = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, я бот-синоптик '
    else:
        greeting = f'Привет, <b>{message.from_user.first_name}</b>, я бот-синоптик '
    bot_prikol.send_message(message.chat.id, greeting, parse_mode='html')

def help_command(message):
    """
    Обработчик команды /help. Отправляет информацию о боте.

    Args:
        message: Объект сообщения от пользователя.
    """
    markup = types.InlineKeyboardMarkup()
    bot_prikol.send_message(message.chat.id, 'Этот бот создан для получения фактов о погоде', reply_markup=markup)

def website(message):
    """
    Обработчик команды /web. Отправляет ссылку на погодный сайт.

    Args:
        message: Объект сообщения от пользователя.
    """
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Погода", url="https://www.accuweather.com/ru/world-weather"))
    bot_prikol.send_message(message.chat.id, 'Проверь прогноз!', reply_markup=markup)

def menu(message):
    """
    Обработчик команды /menu. Отображает меню действий.

    Args:
        message: Объект сообщения от пользователя.
    """
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    low_button = telebot.types.KeyboardButton('/low')
    high_button = telebot.types.KeyboardButton('/high')
    coords_button = telebot.types.KeyboardButton('/coords')
    weather_button = telebot.types.KeyboardButton('/weather')
    markup.add(low_button, high_button, coords_button, weather_button)
    bot_prikol.reply_to(message, "Выберите действие:", reply_markup=markup)

def bot_echo(message):
    """
    Обработчик текстовых сообщений, отправляет эхо-сообщение.

    Args:
        message: Объект сообщения от пользователя.
    """
    bot_prikol.reply_to(
        message, "Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}"
    )
