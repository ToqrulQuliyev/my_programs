import math

action = input('Выберите действие 1.Сложение, 2.Вычетание, 3.Умножение, 4.Деление, 5.Факториал, 6.Квадратный корень: ')
if action != '5':
    if action != '6':
        x = int(input('Введите 1-ое число: '))
        y = int(input('Введите 2-ое число: '))
        if action == '1':
            print(x+y)
        elif action == '2':
            print(x-y)
        elif action == '3':
            print(x*y)
        elif action == '4':
            if y == 0:
                print("Ошибка: деление на ноль невозможно!")
            else:
                print(x / y)

if action == '5':
    fact_num = int(input('Введите число:'))
    print(math. factorial(fact_num))

elif action == '6':
    sqrt_num = int(input('Введите число:'))
    print(math.sqrt(sqrt_num))
