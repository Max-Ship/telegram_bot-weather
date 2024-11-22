from telebot.types import Message
from loguru import logger

from loader import bot


@bot.message_handler(state=None)
@logger.catch
def bot_echo(message: Message) -> None:
    bot.reply_to(
        message, 'Выберите пожалуйста режим работы - введите команду - /menu'
    )
