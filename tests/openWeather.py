import requests

api_key = '01641dfdfe0c8ae874c192935eaeb262'
city = 'campinas'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br"
response = requests.get(url)

if response.status_code == 200:
    answer = response.json()
    description = answer['weather'][0]['description']
    temperature = answer['main']['temp'] - 273.15
    print(f'Campinas está com {description}, temperatura {round(temperature, 2)} graus Celsius')
