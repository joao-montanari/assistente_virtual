import gtts
from playsound import playsound
import requests
import json

url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

data = {
    "prompt": "Qual é a capital da Brasil?",
    "temperature": 0.5,  
    "max_tokens": 30
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

response = requests.get(url, json=data, headers=headers)

if response.status_code == 200:
    resposta = json.loads(response.text)['choices'][0]['text']
    print(resposta)
else:
    print("Error:", response.text)