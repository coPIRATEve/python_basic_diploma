import telebot
from telebot import types

bot_prikol = telebot.TeleBot('6572271155:AAF6KPPIyH6o-MUfWYam8ESJEpowEaBw6dY')

@bot_prikol.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name:
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, ты можешь ' \
               f'написать мне <u>"пошути"</u> и я попробую тебя рассмешить'
    else:
        mess = f'Привет,<b>{message.from_user.first_name}</b>, ты можешь ' \
               f'написать мне <u>"пошути"</u> и я попробую тебя рассмешить'
    bot_prikol.send_message(message.chat.id, mess, parse_mode='html')

@bot_prikol.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.lower() == "пошути":
        bot_prikol.send_message(message.chat.id, 'Я хотел сказать что-то смешное, но лучше посмотри в зеркало',
                                parse_mode='html')
    elif message.text.lower() == "id":
        bot_prikol.send_message(message.chat.id, f"Ну всё, приколист, я вычислил твой ID: {message.from_user.id}",
                                parse_mode='html')
    else:
        bot_prikol.send_message(message.chat.id, 'Такому клоуну, как ты, даже шутить не надо', parse_mode='html')

@bot_prikol.message_handler(content_types=['sticker', 'photo'])
def get_user_media(message):
    bot_prikol.send_message(message.chat.id, "<b>Вау</b>, у тебя, должно быть, нет друзей, если ты делишься таким с ботом",
                            parse_mode='html')

@bot_prikol.message_handler(commands=['web'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Веб-Сайт', url='https://www.google.by/'))
    bot_prikol.send_message(message.chat.id, 'Ознакомьтесь с Веб-Сайтом', reply_markup=markup)

bot_prikol.polling(none_stop=True)
