from database.common.models import db, History

def create_tables_if_not_exist():
    """
    Создает таблицы, если они не существуют.
    """
    with db:
        db.create_tables([History])


if __name__ == "__main__":
    create_tables_if_not_exist()
