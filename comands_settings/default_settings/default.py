import telebot
from telebot import types
from config_data import config

bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN)

def start(message):
    if message.from_user.last_name:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, я бот-синоптик '
    else:
        mess = f'Привет, <b>{message.from_user.first_name}</b>, я бот-синоптик '
    bot_prikol.send_message(message.chat.id, mess, parse_mode='html')

def help_command(message):
    markup = types.InlineKeyboardMarkup()
    bot_prikol.send_message(message.chat.id, 'Этот бот создан для получения фактов о погоде', reply_markup=markup)

def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Погода", url="https://www.accuweather.com/ru/world-weather"))
    bot_prikol.send_message(message.chat.id, 'Проверь прогноз!', reply_markup=markup)

def menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    low_button = telebot.types.KeyboardButton('/low')
    high_button = telebot.types.KeyboardButton('/high')
    coords_button = telebot.types.KeyboardButton('/coords')
    weather_button = telebot.types.KeyboardButton('/weather')
    markup.add(low_button, high_button, coords_button, weather_button)
    bot_prikol.reply_to(message, "Выберите действие:", reply_markup=markup)

def history_handler(bot_prikol, outbase, message):
    user_id = message.from_user.id
    command = message.text
    outbase.create(user_id=user_id, command=command)
    bot_prikol.reply_to(message, "История команды сохранена")

def bot_echo(message):
    bot_prikol.reply_to(
        message, "Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}"
    )
