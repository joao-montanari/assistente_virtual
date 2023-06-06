from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import speech_recognition as sr
import requests
from time import sleep

import core
from nlu.classifier import classify

# Síntese de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)
listener = sr.Recognizer()

def speak(texto):
    engine.say(texto)
    engine.runAndWait()

def comparator(text):
    entity = classify(text)
    separator = entity.split('\\')

    if entity == 'time\getTime':
        speak(core.SystemInfo.get_time())
    elif entity == 'time\getDate':
        speak(core.SystemInfo.get_date())
    elif entity == 'weather\getWeather':
        speak(core.SystemInfo.get_weather())
    elif separator[0] == 'bosch':
        id = separator[1]
        speak(core.SystemInfo.bosch_info(id))

# Reconhecimento de fala

# model = Model('model')
# rec = KaldiRecognizer(model, 16000)

# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
# stream.start_stream()

# Loop do reconhecimento de fala

# while True:
#     data = stream.read(2048)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         result = rec.Result()
#         result = json.loads(result)
        
#         if result is not None:
#             text = result['text']
#             print(text)
#             if text != '':
#                 comparator(text)

# /////////////////////////////////////////////////////////////////////////////

# while True:
#     try:
#         with sr.Microphone() as source:
#             print('Entrada na condição')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice, language='PT-BR')
#             command =  command.lower()
#             if command != []:
#                 print('CAPTURA')
#                 print(command)
#                 comparator(command)
#     except:
#         pass


response = requests.get('http://localhost:7000/question/')
call = response.json()
last_id = response[-1]

while True:
    sleep(1)
    response = requests.get('http://localhost:7000/question/')
    call = response.json()
    verif = call[-1]
    if verif != last_id:
        last_id = verif
        response = requests.get(f"http://localhost:7000/question/{last_id['id']}")
        call = response.json()
        question = call['userQuestion']
        comparator(question)

print('CHAMADA DO COMPARADOR')
comparator('robert bosch')
print('PASSAGEM PELO COMPARADOR')