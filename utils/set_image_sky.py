from loguru import logger

from utils.misc.emoji import weather_emoji


@logger.catch
def image_sky(sky: str) -> str:
    """Function return emoji for weather's data"""

    if sky in weather_emoji:
        image = weather_emoji[sky]
    else:
        image = weather_emoji['other']

    return image
