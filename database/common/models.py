from datetime import datetime
import peewee as pw

# Инициализация базы данных
db = pw.SqliteDatabase('Prikol.db')

class ModelBase(pw.Model):
    # Общая модель для всех таблиц с полем created_at
    created_at = pw.DateField(default=datetime.now)

    class Meta:
        database = db

class History(ModelBase):
    # Модель для таблицы истории
    user_id = pw.IntegerField()
    command = pw.TextField()
    timestamp = pw.DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'history'

# Создание таблицы истории, если она не существует
db.connect()
db.create_tables([History])
