'''Программа загадывает число от 0 до 1000. Необходимо 
угадать число за 10 попыток. Программа должна подсказывать 
«больше» или «меньше» после каждой попытки.'''

TRY = 10
from random import randint
num = randint(0, 1000)
count = 0
for i in range(0, TRY):
    user_num = int(input('Введите число от 0 до 1000: '))
    count += 1
    if user_num == num:
        print(f'Поздравляю! Вы угадали число c {count} попытки!')
        break
    else:
        if user_num < num:
            print('Больше')
        elif user_num > num:
            print('Меньше')
    if count == TRY:
        print(f'Вы не смогли угадать число. Загаданное число {num}.')