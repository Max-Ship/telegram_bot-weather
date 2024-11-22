from telebot.handler_backends import State, StatesGroup


class StateOfUser(StatesGroup):
    weather_now = State()
    weather_days_city = State()
    weather_days_days = State()
    weather_days_aqi = State()
    weather_days_alert = State()
