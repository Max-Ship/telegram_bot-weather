from telebot.types import Message
from loguru import logger

from states import StateOfUser
from loader import bot


@bot.message_handler(commands=["start"])
@logger.catch
def bot_start(message: Message) -> None:
    """Greetings"""
    logger.info('start')

    bot.reply_to(
        message, f'Привет, {message.from_user.full_name}!\nЯ учебный бот, который показывает погоду в любом городе в данное время.\nНапиши мне /help, чтобы узнать как мной пользоваться!')
    bot.delete_state(message.from_user.id)
