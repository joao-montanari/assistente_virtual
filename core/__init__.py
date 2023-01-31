import datetime
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
        answer = 'A previsão de hoje é de tempo nublado'
        return answer