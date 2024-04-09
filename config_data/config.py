import os
from dotenv import load_dotenv, find_dotenv

# Загрузка переменных окружения из файла .env
if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

# Получение значений переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

