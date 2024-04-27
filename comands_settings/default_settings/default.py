import telebot
from telebot import types
from config_data import config
import datetime as dt

bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN)
HISTORY = 'history.txt'


def start(message):
    """
    Обработчик команды /start. Приветствует пользователя и предлагает клавиатуру с командами.

    Args:
        message: Объект сообщения от пользователя.
    """
    greeting = f'Привет, <b>{message.from_user.first_name}</b>! Я бот-синоптик. Воспользуйся кнопками ниже, чтобы получить информацию о погоде или другие сервисы.'
    if message.from_user.last_name:
        greeting = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! Я бот-синоптик. Воспользуйся кнопками ниже, чтобы получить информацию о погоде или другие сервисы.'

    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # Добавляем кнопки
    start_button = types.KeyboardButton('/start')
    help_button = types.KeyboardButton('/help')
    history_button = types.KeyboardButton('/history')
    menu_button = types.KeyboardButton('/menu')

    markup.add(start_button, help_button, history_button, menu_button)
    bot_prikol.send_message(message.chat.id, greeting, parse_mode='html', reply_markup=markup)


def help_command(message):
    """
    Обработчик команды /help. Отправляет информацию о боте.

    Args:
        message: Объект сообщения от пользователя.
    """
    markup = types.InlineKeyboardMarkup()
    bot_prikol.send_message(message.chat.id, 'Этот бот создан для получения фактов о погоде.\n'
                                             'используйте комманду /menu для того чтобы узнать факты о погоде в вашем'
                                             ' городе\n'
                                             'используйте комманду /history для того чтобы увидеть историю ваших '
                                             'последних 10-ти сообщений', reply_markup=markup)

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

def send_history(message):
    """
    Отправляет последние 10 (или меньше, если в файле меньше записей) сообщений пользователю в ответ на команду /history.
    """
    chat_id = message.chat.id
    try:
        with open(HISTORY, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            last_messages = lines[-10:] if len(lines) >= 10 else lines  # Отправляем 10 или меньше строк
            history_content = ''.join(last_messages)
    except FileNotFoundError:
        history_content = "История сообщений пуста."
    except Exception as e:
        history_content = f"Ошибка при чтении файла: {e}"

    if not history_content.strip():
        history_content = "История сообщений пуста или содержит недостаточно данных."

    bot_prikol.send_message(chat_id, "Вот история ваших последних 10-ти сообщений:")
    bot_prikol.send_message(chat_id, history_content)



def record_message_history(message):
    """
     Обработчик текстовых сообщений, сохраняет историю сообщений.

     Args:
         message: Объект сообщения от пользователя.
     """
    if message.text != 'cron':
        with open(HISTORY, "a", encoding='utf-8') as file:
            file.write(str(dt.datetime.now().date()) + '\t')
            file.write(str(dt.datetime.now().time())[:8] + '\t')
            file.write("текст\t")
            if message.from_user.first_name:
                file.write(message.from_user.first_name)
            if message.from_user.last_name:
                file.write(' ' + message.from_user.last_name)
            file.write('\t')
            file.write(str(message.from_user.id) + '\t')
            file.write(message.text + '\n')