from comands_settings import start, help_command, website, menu, min_temp, max_temp, get_weather, get_coord, send_history, record_message_history
from loader import bot_prikol

# Обработчики команд
@bot_prikol.message_handler(commands=['start'])
def start_handler(message):
    record_message_history(message)
    start(message)

@bot_prikol.message_handler(commands=["help"])
def help_command_handler(message):
    record_message_history(message)
    help_command(message)

@bot_prikol.message_handler(commands=['web'])
def website_handler(message):
    record_message_history(message)
    website(message)

@bot_prikol.message_handler(commands=['menu'])
def menu_handler(message):
    record_message_history(message)
    menu(message)

@bot_prikol.message_handler(commands=['low'])
def low_handler(message):
    record_message_history(message)
    min_temp(bot_prikol, message)

@bot_prikol.message_handler(commands=['high'])
def high_handler(message):
    record_message_history(message)
    max_temp(bot_prikol, message)

@bot_prikol.message_handler(commands=['weather'])
def weather_handler(message):
    record_message_history(message)
    get_weather(bot_prikol, message)

@bot_prikol.message_handler(commands=['coords'])
def coords_handler(message):
    record_message_history(message)
    get_coord(bot_prikol, message)

# Обработчик текстовых сообщений

@bot_prikol.message_handler(commands=['history'])
def history_handler(message):
    record_message_history(message)
    send_history(message)

@bot_prikol.message_handler(content_types=['text'])
def handle_text(message):
    record_message_history(message)
