from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()
bot = TeleBot(token=config.BotSettings().bot_token.get_secret_value(),
              state_storage=storage)
