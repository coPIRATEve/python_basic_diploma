import telebot
from config_data import config
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()
bot_prikol = telebot.TeleBot(token=config.BOT_TOKEN, state_storage=storage)

@bot_prikol.message_handler(state=None)
def bot_echo(message):
    bot_prikol.reply_to(
        message, "Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}"
    )
