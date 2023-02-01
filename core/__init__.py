import datetime
import requests
import os

class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = f'São {now.hour} horas e {now.minute} minutos.'
        return answer

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = f'Hoje é dia {now.day} do {now.month} de {now.year}'
        return answer

    @staticmethod
    def get_weather():
        api_key = '01641dfdfe0c8ae874c192935eaeb262'
        city = 'campinas'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br"
        response = requests.get(url)

        if response.status_code == 200:
            answer = response.json()
            description = answer['weather'][0]['description']
            temperature = answer['main']['temp'] - 273.15
            forecast = f'Campinas está com {description} e temperatura de {round(temperature, 2)} graus Celsius'
            return forecast