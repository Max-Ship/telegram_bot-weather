from loguru import logger

from database.model import db, History
from database import commands_db

db_write = commands_db.create()


@logger.catch
def write_db(user_id: str, date: str, city: str, mess: str) -> None:
    """Function add data in two columns db: city and message"""

    data = [{'user_id': user_id, 'date': date, 'city': city, 'message': mess}]
    db_write(db, History, data)
