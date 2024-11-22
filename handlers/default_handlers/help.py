from telebot.types import Message
from loguru import logger

from config_data.config import DEFAULT_COMMANDS
from states import StateOfUser
from loader import bot


@bot.message_handler(commands=["help"])
@logger.catch
def bot_help(message: Message) -> None:
    """Create message on commands - help"""
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(
        message,
        'Привет! Я учебный бот.\
            \nЯ могу работать в двух режимах: \
            \n1) Погода сейчас - погазываю погоду сейчас в выбранном городе,с картиинками \U0001F60E\
            \n В этом режиме (только в этом!!!) доступна комманда - /happy - небольшой список городов \U0001F601\
            \n2) Погода по дням  - провожу опрос: город, количество дней, нужны ли данные о состоянии воздуха и климатических угроз.\
            \nНа основании опроса выдаю данные!' + '\nКоманды:\n' + '\n'.join(text)
    )
