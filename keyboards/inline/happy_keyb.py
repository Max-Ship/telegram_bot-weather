from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from loguru import logger

from utils.misc.emoji import decor_emoji


@logger.catch
def happy_keyboard_markup() -> InlineKeyboardMarkup:
    """Function return inline keuboard"""
    button_1 = InlineKeyboardButton(
        text="Дубай " + decor_emoji["tropical_drink"], callback_data="Дубай")
    button_2 = InlineKeyboardButton(
        text="Стамбул " + decor_emoji["man_surfing"], callback_data="Стамбул")
    button_3 = InlineKeyboardButton(
        text="Анталья " + decor_emoji["grapes"], callback_data="Анталья")
    button_4 = InlineKeyboardButton(
        text="Париж " + decor_emoji["shortcake"], callback_data="Париж")
    button_5 = InlineKeyboardButton(
        text="Хургада " + decor_emoji["clinking_glasses"], callback_data="Хургада")
    button_6 = InlineKeyboardButton(
        text="Дахаб " + decor_emoji["woman_swimming"], callback_data="Дахаб")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2, button_3,
                 button_4, button_5, button_6)
    return keyboard
