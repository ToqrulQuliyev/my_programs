import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Говорите...")
            # Убираем шумоподавление и ставим минимальные тайм-ауты
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

# Вызов функции
result = get_voice_input()
print(result)
