from telebot.types import Message
from loguru import logger
from datetime import datetime

from states import StateOfUser
from keyboards.inline import happy_keyboard_markup
from api import get_data
from utils import image_sky, text_mess_weather_now, write_db
from loader import bot


@bot.message_handler(commands=["happy"], state=[StateOfUser.weather_days_city, StateOfUser.weather_days_days, StateOfUser.weather_days_aqi, StateOfUser.weather_days_alert, None])
@logger.catch
def message_wrong_state(message: Message) -> None:
    """Function create message with inline keybord in a chat"""

    bot.send_message(
        message.from_user.id,
        'Пожалуйста выберите режим - погода сейчас!'
    )


@bot.message_handler(commands=["happy"], state=StateOfUser.weather_now)
@logger.catch
def message_of_happy(message: Message) -> None:
    """Function create message with inline keybord in a chat"""

    bot.send_message(
        message.from_user.id,
        'Куда хочешь поехать?',
        reply_markup=happy_keyboard_markup(),
    )


@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data
    )
)
@logger.catch
def get_weather_of_city(callback_query) -> None:
    """Function calling weather's data
     ofter inline keybord's button press and 
     create this data in a chat"""

    bot.delete_message(callback_query.message.chat.id,
                       callback_query.message.message_id
                       )
    city = callback_query.data

    if get_data.data_weather_now(city) == False:
        bot.send_message(
            callback_query.from_user.id,
            'Извините сервер разорвал соединение или возникла критическая ошибка! Обратитесь в сервис поддержки!')
    elif get_data.data_weather_now(city) == 'status4':
        bot.send_message(
            callback_query.from_user.id,
            'Извините сервер выдал ошибку пользователя!\nПроверте правильно ли Вы написали название города')
    elif get_data.data_weather_now(city) == 'status5':
        bot.send_message(
            callback_query.from_user.id,
            'Извините сервер лег спать. Воспользуйтесь услугой позже')
    else:
        temp, wind, sky = get_data.data_weather_now(city)
        image = image_sky(sky)
        answer = text_mess_weather_now(temp, image, wind)
        text_mess = f'<strong>{city}</strong>\n' + answer

        now = datetime.now()
        write_db(callback_query.from_user.id, now.strftime(
            "%Y-%m-%d; %H:%M"), city, answer)

        bot.send_message(
            callback_query.from_user.id,
            text=text_mess,
            parse_mode='HTML'
        )
