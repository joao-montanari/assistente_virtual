import wikipedia as wp
import pyttsx3

wp.set_lang('pt')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(texto):
    engine.say(texto)
    engine.runAndWait()

while True:
    busca = input('Digite o que deseja saber: ')
    if busca.lower() == 'sair':
        break
    
    resposta = wp.summary(busca, sentences=3)
    print(resposta)
    speak(resposta)