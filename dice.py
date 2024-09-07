import random
import keyboard
import time

dice = ['1', '2', '3', '4', '5', '6']
print("Что-бы бросить кости нажмите 's', что-бы выйти из программы нажмите 'q': ")


def key_event(event):
    if event.name == 's':
        print("\nВы бросили кости 🎲")
        result = random.choice(dice)
        time.sleep(0.3)
        print(f'\nВам выпало:{result}')

keyboard.on_press(key_event)

keyboard.wait('q')