import telebot
from config_data import config
from telebot.storage import StateMemoryStorage
from database.utils.outbase import OutbaseInterface
from database.common.models import History
from comands_settings import start, help_command, website, menu, min_temp, max_temp, get_weather, get_coord

# Создание объекта бота
storage = StateMemoryStorage()
bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN, state_storage=storage)
api = config.API_KEY

# Создание объекта для работы с базой данных
outbase = OutbaseInterface()

# Обработчик всех сообщений пользователя
@bot_prikol.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    command = message.text
    outbase.create(user_id=user_id, command=command)
    if message.text.startswith('/history'):
        send_history(message.chat.id, user_id)
    else:
        bot_prikol.reply_to(message, "Я не понимаю вашу команду")

# Функция отправки истории команд пользователю
def send_history(chat_id, user_id):
    history = outbase.get_user_history(user_id)
    if history:
        bot_prikol.send_message(chat_id, "История ваших команд:\n" + "\n".join(history))
    else:
        bot_prikol.send_message(chat_id, "У вас пока нет истории команд")

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
    min_temp(bot_prikol, message, api)

@bot_prikol.message_handler(commands=['high'])
def high_handler(message):
    max_temp(bot_prikol, message, api)

@bot_prikol.message_handler(commands=['weather'])
def weather_handler(message):
    get_weather(bot_prikol, message, api)

@bot_prikol.message_handler(commands=['coords'])
def coords_handler(message):
    get_coord(bot_prikol, message, api)

# Основной блок кода
if __name__ == "__main__":
    # Создание истории команд для примера
    outbase.create(user_id='1', command='Example message')
    # Получение последних 10 записей истории и вывод на экран
    response = History.select().order_by(History.timestamp.desc()).limit(10)
    for entry in response:
        print(entry.user_id, entry.command)
    # Запуск бота
    bot_prikol.polling()
