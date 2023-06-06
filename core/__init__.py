import datetime
import requests
import os
from urllib import request

# proxy = request.ProxyHandler({'http': 'http://slj4ca:m0nt%40n'+'%40'+'r11024@proxy.br.bosch.com:8080'})
# auth = request.HTTPBasicAuthHandler()
# opener = request.build_opener(proxy, auth, request.HTTPHandler)
# request.install_opener(opener)


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
        else:
            error = 'Infelizmente tive um problema para poder fazer a requisição da resposta. Por favor, tente mais tarde'
            return error
    
    def bosch_info(id):
        response = requests.get(f'http://localhost:5000/answer/{id}')
        if response.status_code == 200:
            call = response.json()
            answer = call['response']
            return answer
        else:
            error = 'Infelizmente tive um problema para poder fazer a requisição da resposta. Por favor, tente mais tarde'
            return error