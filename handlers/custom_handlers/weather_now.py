from telebot.types import Message
from loguru import logger
from datetime import datetime

from api import get_data
from states import StateOfUser
from utils import image_sky, text_mess_weather_now, write_db
from loader import bot


@bot.message_handler(state=StateOfUser.weather_now)
@logger.catch
def get_weather_now(message: Message) -> None:
    """Function create message with weather's data in a chat im mode - weather now"""

    city = message.text.strip().title()
    if get_data.data_weather_now(city) == False:
        bot.send_message(
            message.from_user.id, 'Извините сервер разорвал соединение или возникла критическая ошибка! Обратитесь в сервис поддержки!')
    elif get_data.data_weather_now(city) == 'status4':
        bot.send_message(
            message.from_user.id, 'Извините сервер выдал ошибку пользователя!\nПроверте правильно ли Вы написали название города')
    elif get_data.data_weather_now(city) == 'status5':
        bot.send_message(
            message.from_user.id, 'Извините сервер лег спать. Воспользуйтесь услугой позже')
    else:
        temp, wind, sky = get_data.data_weather_now(city)
        image = image_sky(sky)
        text = f'<strong>{city}</strong>\n' + \
            text_mess_weather_now(temp, image, wind)

        now = datetime.now()
        write_db(message.from_user.id, now.strftime(
            "%Y-%m-%d; %H:%M"),  city, text)

        bot.send_message(
            message.from_user.id, text=text, parse_mode='HTML')
