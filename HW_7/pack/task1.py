# ✔Напишите функцию, которая заполняет файл (добавляет в конец)
# случайными парами чисел. ✔Первое число int, второе - float разделены
# вертикальной чертой. ✔Минимальное число - -1000, максимальное - +1000.
# ✔Количество строк и имя файла передаются как аргументы функции.

__all__ = ['digits']

from random import randint, uniform
import os

MIN_VALUE = -1000
MAX_VALUE = 1000


def digits(count_rows: int, file_name: str, dir_name: str):
    file_path = os.path.join(dir_name, file_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if not os.path.exists(file_path):
        with open(file_path, 'a', encoding='utf-8') as f:
            for i in range(count_rows):
                f.write(
                    f'{randint(MIN_VALUE, MAX_VALUE)}|{uniform(MIN_VALUE,MAX_VALUE)}\n')


if __name__ == '__main__':
    digits(5, 'file_1.txt',
            'D:\Geek Brains\погружение в Python\immersion_in_python\HW_7\Doc')
