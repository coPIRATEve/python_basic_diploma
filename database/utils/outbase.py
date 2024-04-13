from typing import Dict, List, TypeVar
from peewee import ModelSelect
from database.common.models import ModelBase
from ..common.models import db

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
