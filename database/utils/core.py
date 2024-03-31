from database.common.models import db, History
from datetime import datetime

class OutbaseInterface():  # Исправлено название класса
    @staticmethod
    def create(data):
        return History.create(timestamp=datetime.now(), number=data['number'], message=data['message'])  # Исправлены аргументы

db.connect()
db.create_tables([History])

outbase = OutbaseInterface()  # Исправлен вызов

if __name__ == "__main__":  # Исправлено условие
    pass
