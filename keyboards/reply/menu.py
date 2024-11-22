from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from loguru import logger

from utils.misc.emoji import decor_emoji


@logger.catch
def menu_keyboard() -> ReplyKeyboardMarkup:
    """Function return inline keuboard"""
    button_1 = KeyboardButton(
        text="Погода сейчас" + decor_emoji["sun_behind_small_cloud"])

    button_2 = KeyboardButton(
        text="Погода по дням" + decor_emoji["thermometer"])
    button_3 = KeyboardButton(
        text="О боте" + decor_emoji["robot"])

    keyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_reply.add(button_1, button_2, button_3)
    return keyboard_reply
