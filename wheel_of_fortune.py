import random
import time

var_count = int(input("Введите сколько вариантов вам нужно: "))
if var_count <= 1:
    print('Это действие не имеет смысла! Попробуйте снова')
    exit()

all_variants = []
x = 0

for i in range(var_count):
    x += 1
    user_input = input(f"Введите {x} вариант: ")
    all_variants.append(user_input)

print("Колесо крутится 🎡")
time.sleep(0.6)
print(random.choice(all_variants))
