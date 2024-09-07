import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    print('-------')
    print(f'Имя: {voice.name}')
    print(f'ID: {voice.id}')
    print(f'Язык: {voice.languages}')
    print(f'Пол: {voice.gender}')
    print(f'Возраст: {voice.age}')

engine.say('Привет')

engine.runAndWait()
