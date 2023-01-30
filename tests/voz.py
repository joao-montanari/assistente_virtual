import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voice') 
#engine.setProperty('voice', voices[-2])

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='PT-BR')
            command =  command.lower()
            if 'avila' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_avila():
    command = take_command()
    print(command)
    if 'tocar' in command:
        song = command.replace('tocar', '')
        talk('tocando ' + song)
        pywhatkit.playonyt(song)
    elif 'horas' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('O horário atual é de ' + time)
    elif 'o que é' in command:
        person = command.replace('quem é', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
run_avila()