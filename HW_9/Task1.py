# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой
# тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл

from random import randint as rnd
from math import pow
import csv
import json

LINES = 100
ARGS = 3
MIN_LIMIT = -100
MAX_LIMIT = 100


def rnd_numbers(f_csv):
    lst = []
    for _ in range(ARGS):
        lst.append(rnd(MIN_LIMIT, MAX_LIMIT + 1))
    for i in range(LINES):
        for j in range(ARGS):
            lst[j] = rnd(MIN_LIMIT, MAX_LIMIT + 1)
            if lst[j] == 0:
                lst[j] = 1
        with open(f_csv, 'a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f, delimiter=' ')
            csv_write.writerow(lst)


def deco(func):
    _dct = {}

    def wrapper(*args):
        a, b, c = args
        x1, x2 = func(*args)
        _dct[f'{a = }, {b = }, {c = }'] = f'{x1 = }, {x2 = }'
        return _dct

    return wrapper


def save_json(func):
    def wrapper(*args, **kwargs):
        with open('the_quadratic_equation.json', 'w', encoding='utf-8') as f:
            res = func(*args, **kwargs)
            json.dump(res, f, ensure_ascii=False, indent=2)

    return wrapper


@save_json
@deco
def get_roots(a, b, c):
    d = pow(b, 2) - (4 * a * c)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    x1 = complex(round(x1.real), round(x1.imag))
    x2 = complex(round(x2.real), round(x2.imag))
    return x1, x2


if __name__ == '__main__':
    rnd_numbers('arguments.csv')
    with open('arguments.csv', 'r', encoding='utf-8') as f:
        csv_read = csv.reader(f, delimiter=' ')
        for line in csv_read:
            a, b, c = map(int, line)
            get_roots(a, b, c)
