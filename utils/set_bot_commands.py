from telebot.types import BotCommand
from loguru import logger

from config_data.config import DEFAULT_COMMANDS


@logger.catch
def set_default_commands(bot) -> None:
    """Function created list of comamands of bot in chat"""

    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
