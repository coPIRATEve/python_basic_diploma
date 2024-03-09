import telebot
from telebot import types
from config_data import config
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()
bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN, state_storage=storage)

@bot_prikol.message_handler(commands=["help"])
def help(message):
   markup = types.InlineKeyboardMarkup()
   button1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
   markup.add(button1)
   mess = bot_prikol.send_message(message.chat.id, 'Задайте вопрос боту.', reply_markup=markup)

@bot_prikol.callback_query_handler(func=lambda call: call.data == "get_help")
def callback_get_help(call):
    help(call.message)
