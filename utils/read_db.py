from loguru import logger

from database.model import db, History
from database import commands_db

db_read = commands_db.retrieve()


@logger.catch
def read_db(item_id: str) -> list:
    """Read data in db and give data to user"""

    retrieved = db_read(db, History, History.user_id, History.date,
                        History.city, History.message)
    db_list = [
        f"ID: {elem.user_id}.\nВремя: {elem.date}.\nГород: {elem.city}.\n{elem.message}\n +{'-'*25}+\n" for elem in retrieved if int(item_id) == int(elem.user_id)]

    return db_list


if __name__ == '__main__':
    read_db()
