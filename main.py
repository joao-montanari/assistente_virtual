from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
from nlu.classifier import classify

# Síntese de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

reference = {
    'time\getTime' : core.SystemInfo.get_time(),
    'time\getDate' : core.SystemInfo.get_date(),
    'weather\getWeather' : core.SystemInfo.get_weather(),
}

def speak(texto):
    engine.say(texto)
    engine.runAndWait()

def choice(text):
    entity = classify(text)
      
    if entity == 'time\getTime':
        speak(core.SystemInfo.get_time())
    elif entity == 'time\getDate':
        speak(core.SystemInfo.get_date())
    else:
        speak(text)
        print(text)

def comparator(text):
    entity = classify(text)

    for i in reference:
        if i == entity:
            speak(reference[entity])

# Reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        
        if result is not None:
            text = result['text']
            print(text)
            comparator(text)



# print(rec.FinalResult())