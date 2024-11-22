from loader import bot
from telebot.types import Message
from loguru import logger
import os
import re


@logger.catch
def text_mess_weather_now(temp: str, image: str, wind: str) -> str:
    """Function return text of message in mode - weather now"""

    return f'<code>Температура</code>: <strong>{temp}</strong>°. {image}\n<code>Скорость ветра</code>: <strong>{wind}</strong> м/с.'


@logger.catch
def text_mess_weather_by_days(data_weather: list) -> str:
    """Function return text of message in mode - weather by days"""

    text = ''
    for item in data_weather:
        text += f'<code>Дата</code>: {item["date"]}.\
            \n<code>Температура</code>: {item["temp_min"]}° - {item["temp_max"]}°. \
            \n<code>Скорость ветра</code>: {item["wind"]} м/с. \
            \n<b><i>{item["sky"]}</i></b>\n'

    return text


@logger.catch
def text_mess_aqi(aqi: list) -> str:
    """Function return text of message aqi in mode - weather by days"""

    text = '<b>---Состояние воздуха---</b>'

    for item in aqi:
        if item['data'] == {'aqi_data': 'null'}:
            text += f'\n<strong>Данных пока НЕТ!</strong>'
        else:
            text += f'\n<code>Окись углерода:</code> {item["data"]["co"]} мкг/м3.\
                \n<code>Диоксид азота:</code> {item["data"]["no2"]} мкг/м3.\
                \n<code>Озон:</code> {item["data"]["o3"]} мкг/м3.\
                \n<code>Диоксид серы:</code> {item["data"]["so2"]} мкг/м3.\
                \n<code>Мелкая взвесь:</code> {item["data"]["pm2_5"]} мкг/м3.\
                \n<code>Крупная взвесь:</code> {item["data"]["pm10"]} мкг/м3.\
                \n<code>Индекс качества воздуха:</code> {item["data"]["us-epa-index"]}.\
                \n<code>Индекс загрязнения воздуха:</code> {item["data"]["gb-defra-index"]}.'

    text += '\n<i>Расшифровка индекса:</i>\
        \n1 - означает <i><b>Хорошо</b></i>\
        \n2 - означает <i><b>Умеренно</b></i>\
        \n3 - означает <i><b>Вредно для чувствительной группы</b></i>\
        \n4 - означает <i><b>Вредно</b></i>\
        \n5 - означает <i><b>Очень вредно</b></i>\
        \n6 - означает <i><b>Опасно</b></i>'
    return text


@logger.catch
def text_mess_alert(alerts: list) -> str:
    """Function return text of message alert in mode - weather by days"""

    if len(alerts) == 0:
        return '\nУгроз природных катаклизмов <b>нет</b>!'
    else:
        text = ''
        for item in alerts:
            text += f'\n<strong>Усиление:</strong> {item["effective"]}.\
        \n<strong>Ослабление:</strong> {item["expires"]}.\
        \n<strong>Описание:</strong> {item["desc"]}.'

    return text


@logger.catch
def get_mess_or_file(message: Message, item_id: str,  mess_text: str, city: str or None) -> None:
    """Function create message with data in the db in chat or write data in file for user`s save"""

    if len(mess_text) < 4096:
        if (city):
            bot.send_message(message.from_user.id,
                             text=f"<strong>{city.title()}</strong>\n" + mess_text, parse_mode='HTML')
        else:
            bot.send_message(message.from_user.id,
                             text=mess_text, parse_mode='HTML')
    else:
        bot.send_message(message.from_user.id, 'Извините Ваши данные очень большие!\n\
        Не могу вывести в чат!\nСкачайте их пожалуйста файлом!')

        with open(f'large_message_{message.from_user.id}.txt', 'w', encoding='utf8') as file:
            if (city):
                file.write(f"{city}\n" + re.sub(r'<[^>]+>', '', mess_text))
            else:
                file.write(re.sub(r'<[^>]+>', '', mess_text))

        with open(f'large_message_{message.from_user.id}.txt', 'rb') as file:
            bot.send_document(message.chat.id, file)

        if (f'large_message_{message.from_user.id}.txt'):
            os.remove(f'large_message_{message.from_user.id}.txt')


if __name__ == '__main__':
    text_mess_weather_now()
    text_mess_weather_by_days()
    text_mess_aqi()
    text_mess_alert()
    get_mess_or_file()
