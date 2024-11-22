from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from loguru import logger
from time import sleep

from states.states import StateOfUser
from keyboards.reply import menu_keyboard
from utils.misc.emoji import decor_emoji


@bot.message_handler(commands=['menu'])
@logger.catch
def menu(message: Message) -> None:
    """menu mode bot"""

    bot.send_message(
        message.from_user.id,
        'Выберите режим работы!',
        reply_markup=menu_keyboard()
    )
    bot.delete_state(message.from_user.id)


@bot.message_handler(func=lambda message: message.text == 'О боте' + decor_emoji['robot'], state=None)
@logger.catch
def about_bot(message: Message) -> None:
    """About bot"""

    bot.send_message(
        message.from_user.id,
        'Здесь божественное описание сие божественного бота!!!',
        reply_markup=ReplyKeyboardRemove())
    sleep(1.5)
    bot.send_message(
        message.from_user.id,
        'Все права принадлежат тому кому они принадлежат и не пренадлежат тому кому они не принадлежат!!!')
    sleep(1.5)
    bot.send_message(
        message.from_user.id,
        'Возьмите меня на рабооту!!!')
    sleep(1.5)
    bot.send_message(
        message.from_user.id,
        'ПОЖЖЖЖААААЛУУУЙССТАА!!!')
    sleep(1.5)
    bot.send_message(
        message.from_user.id,
        decor_emoji['face_holding_back_tears'])


@bot.message_handler(func=lambda message: message.text == 'Погода сейчас' + decor_emoji['sun_behind_small_cloud'], state=None)
@logger.catch
def set_weather_now(message: Message) -> None:
    """mode: weather_now - activated"""

    bot.set_state(message.from_user.id,
                  StateOfUser.weather_now)
    bot.send_message(
        message.from_user.id,
        'Привет! Напиши любой город и я покажу тебе погоду в этом городе сейчас!',
        reply_markup=ReplyKeyboardRemove())


@bot.message_handler(func=lambda message: message.text == 'Погода по дням' + decor_emoji['thermometer'], state=None)
@logger.catch
def set_weather_days(message: Message) -> None:
    """mode: weather_by_days - activated"""

    bot.set_state(message.from_user.id,
                  StateOfUser.weather_days_city)
    bot.send_message(
        message.from_user.id,
        'Привет! Напиши любой город, количество дней и я выведу тебе всю информацию!',
        reply_markup=ReplyKeyboardRemove())
