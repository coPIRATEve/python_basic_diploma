from database.common.models import db, History
from datetime import datetime


class OutbaseInterface:
    @staticmethod
    def create(user_id, command):
        """
        Создает новую запись истории команд пользователя.

        Args:
            user_id (str): Идентификатор пользователя.
            command (str): Команда пользователя.
        """
        History.create(user_id=user_id, command=command, timestamp=datetime.now())

    @staticmethod
    def get_user_history(user_id):
        """
        Получает историю последних 10 команд пользователя.

        Args:
            user_id (str): Идентификатор пользователя.

        Returns:
            list: Список последних 10 команд пользователя.
        """
        history = History.select().where(History.user_id == user_id).order_by(History.timestamp.desc()).limit(10)
        return [entry.command for entry in history]


def create_tables_if_not_exist():
    """
    Создает таблицы, если они не существуют.
    """
    with db:
        db.create_tables([History])


if __name__ == "__main__":
    create_tables_if_not_exist()
