import logging
import telebot
from telebot import types
from config_data import config
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()
bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN, state_storage=storage)

@bot_prikol.message_handler(commands=['main_menu'])
#главное меню
def main_menu(message):
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton(text='Погода', callback_data="go_to_website"))
    key.add(types.InlineKeyboardButton(text='help', callback_data="get_help"))
    mess = bot_prikol.send_message(message.chat.id, 'Нажми кнопку', reply_markup=key)
    logging.info((message.chat.id, mess))

@bot_prikol.message_handler(commands=['web'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Погода", url="https://www.kinopoisk.ru/?utm_referrer=yandex.by"))
    bot_prikol.send_message(message.chat.id, 'Проверь прогноз!', reply_markup=markup)

@bot_prikol.callback_query_handler(func=lambda call: call.data == "go_to_website")
def callback_go_to_website(call):
    website(call.message)
