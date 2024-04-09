from typing import Dict, List, TypeVar
from peewee import ModelSelect
from database.common.models import ModelBase
from ..common.models import db
from database.common.models import History

T = TypeVar("T")


def store_data(database: db, model: T, *data: List[Dict]) -> None:
    """
    Сохраняет данные в базу данных.

    Args:
        database: Объект базы данных.
        model: Модель данных для сохранения.
        data: Данные для сохранения.
    """
    with database.atomic():
        model.insert_many(data).execute()


def retrieve_all_data(database: db, model: T, *columns: ModelBase) -> ModelSelect:
    """
    Извлекает все данные из базы данных.

    Args:
        database: Объект базы данных.
        model: Модель данных для извлечения.
        columns: Список столбцов для извлечения.

    Returns:
        Модель выборки данных.
    """
    with database.atomic():
        response = model.select(*columns)
    return response


class OutbaseInterface:
    @staticmethod
    def create(user_id, command):
        """
        Создает запись в истории команд пользователя.

        Args:
            user_id: Идентификатор пользователя.
            command: Выполненная команда.
        """
        History.create(user_id=user_id, command=command)

    @staticmethod
    def get_user_history(user_id):
        """
        Получает историю команд пользователя.

        Args:
            user_id: Идентификатор пользователя.

        Returns:
            Список последних команд пользователя.
        """
        history = History.select().where(History.user_id == user_id).order_by(History.timestamp.desc()).limit(10)
        return [entry.command for entry in history]


if __name__ == "__main__":
    pass
