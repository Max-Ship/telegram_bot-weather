from telebot.types import Message
from loguru import logger
from datetime import datetime

from api.get_data import data_weather_by_days
from states import StateOfUser
from utils import text_mess_weather_by_days, text_mess_aqi, text_mess_alert, get_mess_or_file, write_db
from loader import bot


@bot.message_handler(state=StateOfUser.weather_days_city)
@logger.catch
def get_city(message: Message) -> None:
    """Function save status - weather_days_city"""

    city = message.text.title()
    if data_weather_by_days(city, days=1, status_aqi='no', status_alert='no') == 'status4':
        bot.send_message(message.from_user.id,
                         text='Проверте название города')
    else:
        bot.send_message(
            message.from_user.id, text='Запомнил. Теперь введите колчество дней (от 1 до 3).')
        bot.set_state(message.from_user.id,
                      StateOfUser.weather_days_days)

        with bot.retrieve_data(message.from_user.id) as data:
            data['weather_days_city'] = message.text


@bot.message_handler(state=StateOfUser.weather_days_days)
@logger.catch
def get_days(message: Message) -> None:
    """Function save status - weather_days_days"""

    if message.text.startswith('/') or message.text.isalpha() or int(message.text) > 3:
        bot.send_message(message.from_user.id,
                         text='Введите целое число от 1 до 3')
    else:
        bot.send_message(
            message.from_user.id, text='Запомнил. Вам нужны данные качества воздуха на этот период? (да или нет)')
        bot.set_state(message.from_user.id,
                      StateOfUser.weather_days_aqi)

        with bot.retrieve_data(message.from_user.id) as data:
            data['weather_days_days'] = message.text


@bot.message_handler(state=StateOfUser.weather_days_aqi)
@logger.catch
def get_aqi(message: Message) -> None:
    """Function save status - weather_days_aqi"""

    if message.text.isdigit() or message.text.lower() not in ['да', 'yes', 'no', 'нет']:
        bot.send_message(message.from_user.id,
                         text='Введите да или нет!')
    else:
        bot.send_message(
            message.from_user.id, text='Запомнил. Вам нужны данные об угрозах погодных явлений? (да или нет)')
        bot.set_state(message.from_user.id,
                      StateOfUser.weather_days_alert)

        with bot.retrieve_data(message.from_user.id) as data:
            data['weather_days_aqi'] = message.text.lower()


@bot.message_handler(state=StateOfUser.weather_days_alert)
@logger.catch
def get_aqi(message: Message) -> None:
    """Function save status - weather_days_alert and create data of message in chat"""

    if message.text.isdigit() or message.text.lower() not in ['да', 'yes', 'no', 'нет']:
        bot.send_message(message.from_user.id,
                         text='Введите да или нет!')
    else:

        with bot.retrieve_data(message.from_user.id) as data:
            data['weather_days_alert'] = message.text.lower()

        city = data['weather_days_city']
        days = data['weather_days_days']
        aqi_status = data['weather_days_aqi']
        alert_status = data['weather_days_alert']
        answer_user = {
            'yes': 'yes',
            'да': 'yes',
            'no': 'no',
            'нет': 'no'
        }

        result = data_weather_by_days(
            city, days, answer_user[aqi_status], answer_user[alert_status])
        if isinstance(result, tuple):
            data_weather, aqi, alerts = result
            text_message = text_mess_weather_by_days(data_weather)

            if aqi != None:
                text_message += text_mess_aqi(aqi)

            if alerts != None:
                text_message += text_mess_alert(alerts)

            now = datetime.now()
            write_db(message.from_user.id, now.strftime(
                "%Y-%m-%d; %H:%M"), city.title(), text_message)

            get_mess_or_file(message, message.from_user.id,
                             text_message, city=city)

            bot.delete_state(message.from_user.id)
            bot.set_state(message.from_user.id,
                          StateOfUser.weather_days_city)
        elif result is False:
            bot.send_message(message.from_user.id,
                             text='Извините! Произошла непредвиденная ошибка! Обратитесь в службу поддуржки')
            bot.delete_state(message.from_user.id)
            bot.set_state(message.from_user.id,
                          StateOfUser.weather_days_city)
