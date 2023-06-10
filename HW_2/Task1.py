'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
строковое представление. Функцию hex используйте для проверки своего результата.'''

NUM_A = 10
NUM_B = 11
NUM_C = 12
NUM_D = 13
NUM_E = 14
NUM_F = 15

user_num = int(input('Введите целове число: '))
res = ''
print(hex(user_num))

while user_num > 0:
    dev = user_num % 16
    if dev == NUM_A:
        res += str('A')
    elif dev == NUM_B:
        res += str('B')
    elif dev == NUM_C:
        res += str('C')
    elif dev == NUM_D:
        res += str('D')
    elif dev == NUM_E:
        res += str('E')
    elif dev == NUM_F:
        res += str('F')
    else:
        res += str(dev)
    user_num //= 16

print(res[::-1])