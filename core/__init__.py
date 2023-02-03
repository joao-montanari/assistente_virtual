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
        else:
            error = 'Infelizmente tive um problema para poder fazer a requisição da previsão do tempo. Por favor, tente mais tarde'
            return error
    
    def get_ceo():
        answer = 'O Doutor Stefan Hartung é presidente do conselho de administração e acionista da Robert Bosch, G1 desde 1º de janeiro de 2022. Suas responsabilidades incluem estratégia corporativa, comunicações corporativas, assuntos governamentais e desenvolvimento de tecnologia. Ele também é responsável pela pesquisa corporativa, engenharia avançada, gerenciamento de qualidade corporativa e pelo departamento corporativo de Fabricação de Tecnologia. Além disso, ele é responsável pela subsidiária Bosch Healthcare Solutions e pelas operações da Bosch na China.'
        return answer
    
    def get_job():
        answer = 'A Bosch atua em diferentes ramos da industria. Entre elas ela se contra desenvolvendo acessórios e ferramentas elétricas, negócios industriais, sistemas de segurança, soluções técnicas para manufatura, tecnologia de acionamento e controle, soluções de software e ainda atuando entre outros ramos.'
        return answer