import time
import pyttsx3
import speech_recognition as sr

# Инициализация и настройка pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume', 0.9)

def health_assistant(symptom):
    recommendations = {
        "голова": "Примите Ибупрофен или Парацетамол и отдохните в тёмном и тихом месте, Пейте больше воды.",
        "зубы": "Промойте рот соленой водой, примите нимесил или обезболивающее, Если боль не проходит, обратитесь к стоматологу.",
        "спина": "Отдохните, примите теплую ванну или приложите теплый компресс, Попробуйте лёгкие упражнения на растяжку.",
        "живот": "Избегайте тяжелой пищи, пейте больше воды, Можно принять активированный уголь или спазмолитики, Если боль не проходит, обратитесь к врачу.",
        "грудь": "Срочно обратитесь к врачу, Боль в груди может быть опасной!",
        "горло": "Пейте тёплую воду или чай с мёдом, Полоскайте горло солёной водой, Можно использовать спреи или таблетки для горла (например Гексорал или Стрепсилс).",
        "суставы": "Примите ибупрофен или другое противовоспалительное средство, Приложите холодный компресс, Если боль продолжается, обратитесь к врачу.",
        "уши": "Используйте капли для ушей с обезболивающим (например Отипакс), Если боль усиливается или сопровождается лихорадкой, обратитесь к врачу.",
        "глаз": "Промойте глаз чистой водой или физраствором, Если раздражение или боль не проходят, обратитесь к офтальмологу.",
        "тошнота": "Пейте маленькими глотками воду или чай, Можно принять препараты против тошноты (например, Церукал), и не ложитесь, Если состояние не улучшается, обратитесь к врачу.",
        "кашель": "Пейте много тёплой жидкости, используйте сиропы от кашля (например Корень солодки) или ингаляции.",
        "насморк": "Используйте спреи для промывания носа (например Снуп).",
        "усталость": "Отдохните, больше спите, Пейте больше воды и включите в рацион питательные продукты.",
        "головокружение": "Отдохните в тихом месте, Избегайте резких движений, Если состояние не проходит, обратитесь к врачу.",
    }

    if symptom.lower() in recommendations:
        engine.say(recommendations[symptom])
        engine.runAndWait()
        return recommendations[symptom.lower()]
    else:
        engine.say("Я не знаю лечения для этого симптома. Обратитесь к врачу.")
        engine.runAndWait()
        return "Я не знаю лечения для этого симптома. Обратитесь к врачу."

engine.say("Что у вас болит?")
engine.runAndWait()

def get_voice_input2():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Говорите...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        return recognizer.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        return "Не удалось распознать речь."
    except sr.RequestError:
        return "Ошибка сервиса распознавания."
    except OSError as e:
        return f"Ошибка микрофона: {e}"
    except sr.WaitTimeoutError:
        return "Превышено время ожидания."

result = get_voice_input2()
print(result)

user_symptom = result
advice = health_assistant(user_symptom)
print(advice)

# Доп. проверка состояния человека через 30 минут
time.sleep(0.5)
engine.say("Прошла ли ваша боль?: ")
engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Говорите...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        return recognizer.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        return "Не удалось распознать речь."
    except sr.RequestError:
        return "Ошибка сервиса распознавания."
    except OSError as e:
        return f"Ошибка микрофона: {e}"
    except sr.WaitTimeoutError:
        return "Превышено время ожидания."

result2 = get_voice_input()
print(result2)

x = result2.lower()

if x == 'да':
    print("Хорошо. Я отключаюсь, пока")
    engine.say("Хорошо. Я отключаюсь, пока")
    engine.runAndWait()
elif x == 'нет':
    print("Если вы следовали всем рекомендациям и боль не прошла, обратитесь к врачу!")
    engine.say("Если вы следовали всем рекомендациям и боль не прошла, обратитесь к врачу!")
    engine.runAndWait()
else:
    print("Извините, я не понял ваш ответ. Если боль не проходит, обратитесь к врачу.")
    engine.say("Извините, я не понял ваш ответ. Если боль не проходит, обратитесь к врачу.")
    engine.runAndWait()
