import os
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings
from pydantic import SecretStr, StrictStr

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


class SiteSettings(BaseSettings):
    api_key_w_n: SecretStr = os.getenv("API_KEY_WEATHER_NOW")
    api_host_w_n: StrictStr = os.getenv("API_HOST_WEATHER_NOW")

    api_key_w_d: SecretStr = os.getenv("API_KEY_WEATHER_BY_DAYS")
    api_host_w_d: StrictStr = os.getenv("API_HOST_WEATHER_BY_DAYS")


class BotSettings(BaseSettings):
    bot_token: SecretStr = os.getenv("BOT_TOKEN")


DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("menu", "Выбор режима"),
    ("happy", "Города для отпуска. Режим: Погода сейчас!"),
    ("history", "История запросов. Режим должен быть не выбран!")
)

SECRET_COMMAND: StrictStr = os.getenv("GET_DB")
