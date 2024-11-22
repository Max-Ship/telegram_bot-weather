from loader import bot
from telebot.types import Message
from loguru import logger
import os

from utils.read_db import read_db
from utils import get_mess_or_file


@bot.message_handler(commands=['history'])
@logger.catch
def history(message: Message) -> None:
    arhiv = read_db(message.from_user.id)
    mess_text = ''
    for mess in arhiv:
        mess_text += mess+"\n"

    get_mess_or_file(message, message.from_user.id, mess_text, city=None)
