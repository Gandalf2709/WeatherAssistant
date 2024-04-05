import pyttsx3
import requests

engine = pyttsx3.init()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={53.555715}&lon={10.240009}&appid={70aecda64f9e9faedc48a3a4723d8ecb}")


def say(text: str, rate: int, volume: float, voice: int):
    engine.setProperty('rate', rate)  # setting up new voice rate
    engine.setProperty('volume', volume/100)  # setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')  # getting details of current voice
    if voice == 0:
        engine.setProperty('voice', voices[0].id)   # changing index, changes voices. o for german
    elif voice == 1:
        engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for english
    engine.say(text)
    engine.runAndWait()


engine.stop()
