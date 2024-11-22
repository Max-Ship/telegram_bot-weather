from typing import Dict, List, TypeVar

from peewee import ModelSelect
from loguru import logger

from .model import db, ModelBase


T = TypeVar('T')


@logger.catch
def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    """create columns in db"""
    with db.atomic():
        model.insert_many(*data).execute()


@logger.catch
def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    """get data in db"""
    with db.atomic():
        response = model.select(*columns)

    return response


class Commands():

    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == '__main__':
    _store_date()
    _retrieve_all_data()
    Commands()
