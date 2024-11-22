from loader import bot
from loguru import logger

import handlers
from handlers.default_handlers import echo
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands

logger.add(
    'debug.log', format='{time} {level} {message}', level="DEBUG", serialize=True)

if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()
