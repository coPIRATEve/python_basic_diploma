import logging
import telebot
from telebot import types
from venv.settings import SiteSettings

# Загрузка настроек из файла .env
settings = SiteSettings()

bot_prikol = telebot.TeleBot(settings.tg_api.get_secret_value())

@bot_prikol.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, я бот-киноман '
    else:
        mess = f'Привет, <b>{message.from_user.first_name}</b>, я бот-киноман '
    bot_prikol.send_message(message.chat.id, mess, parse_mode='html')

@bot_prikol.message_handler(commands=['main_menu'])
#главное меню
def main_menu(message):
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton(text='Кинопоиск', callback_data="go_to_website"))
    key.add(types.InlineKeyboardButton(text='help', callback_data="get_help"))
    mess = bot_prikol.send_message(message.chat.id, 'Нажми кнопку', reply_markup=key)
    logging.info((message.chat.id, mess))

@bot_prikol.message_handler(commands=["help"])
def help(message, res=False):
   markup = types.InlineKeyboardMarkup()
   button1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
   markup.add(button1)
   mess = bot_prikol.send_message(message.chat.id, 'Задайте вопрос боту.', reply_markup=markup)
   bot_prikol.register_next_step_handler(mess, message.chat.id)

@bot_prikol.message_handler(commands=['web'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Кинопоиск", url="https://www.kinopoisk.ru/?utm_referrer=yandex.by"))
    bot_prikol.send_message(message.chat.id, 'Лучшие фильмы здесь!', reply_markup=markup)

@bot_prikol.callback_query_handler(func=lambda call: call.data == "go_to_website")
def callback_go_to_website(call):
    website(call.message)

@bot_prikol.callback_query_handler(func=lambda call: call.data == "get_help")
def callback_get_help(call):
    help(call.message)

bot_prikol.polling(none_stop=True)

