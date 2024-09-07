import random

x = ['камень', 'ножницы', 'бумага']

user_input = input("Выберите: камень🗿, ножницы✂️ или бумага📃?:\n").lower()
while user_input not in ['камень', 'ножницы', 'бумага']:
    print("Неверный выбор. Попробуйте снова.")
    user_input = input("Выберите: камень, ножницы или бумага? ").lower()

game_choice = random.choice(x)

print(f"Вы выбрали: {user_input}")
print(f"Компьютер выбрал: {game_choice}")

if user_input == game_choice:
    print("Ничья!")
elif (user_input == 'камень' and game_choice == 'ножницы') or \
     (user_input == 'ножницы' and game_choice == 'бумага') or \
     (user_input == 'бумага' and game_choice == 'камень'):
    print("Вы победили🏆!")
else:
    print("Победил Компьютер🏆 !")
