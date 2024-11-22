import requests
from typing import List, Dict, Union, Tuple, Optional
from loguru import logger

from config_data import config


site = config.SiteSettings()


@logger.catch
def data_weather_now(city: str) -> Union[str, bool, Tuple[Union[str, float]]]:
    """Function return API data: str - temp, wind, sky"""
    url = site.api_host_w_n

    qs = {'q': city, 'appid': site.api_key_w_n.get_secret_value(),
          'units': 'metric'}
    try:
        response = requests.get(url, params=qs)
        status = str(response.status_code)

        if status.startswith('4'):
            return 'status4'
        elif status.startswith('5'):
            return 'status5'
        else:
            data = response.json()
            temp = data['main']['temp']
            wind = data['wind']['speed']
            sky = data['weather'][0]['main']
            return temp, wind, sky
    except:
        return False


@logger.catch
def data_weather_by_days(city: str, days: str, status_aqi: str, status_alert: str) -> Union[
    str,
    Tuple[List[Dict[str, Union[str, float]]],
          Optional[List[Dict[str, Union[str, float]]]],
          Optional[List[Dict[str, str]]]],
    bool
]:
    """Function return API data: str - temp, wind, sky"""
    url = site.api_host_w_d

    qs = {'key': site.api_key_w_d.get_secret_value(),
          'q': city,
          'days': days,
          'aqi': status_aqi,
          'alerts': status_alert,
          'lang': 'ru'}
    try:
        response = requests.get(url, params=qs)
        status = str(response.status_code)

        if status.startswith('4'):
            return 'status4'
        elif status.startswith('5'):
            return 'status5'
        else:
            data = response.json()
            answer_data = [{'date': elem['date'], 'temp_min': elem['day']['mintemp_c'], 'temp_max':  elem['day']['maxtemp_c'], 'wind': elem['day']['maxwind_kph'],  'sky': elem['day']['condition']['text']}
                           for elem in data['forecast']['forecastday']]
            aqi = None
            if status_aqi == 'yes':
                aqi = [{'data': data['current']['air_quality']}]

            alerts = None
            if status_alert == 'yes':
                alerts = [{'effective': elem['effective'],  'expires': elem['expires'], 'desc': elem['desc']}
                          for elem in data['alerts']['alert']]

            return answer_data, aqi, alerts
    except:
        return False
