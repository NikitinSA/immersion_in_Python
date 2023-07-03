'''Напишите функцию, которая преобразует pickle файл хранящий список словарей в
табличный csv файл. Для тестированию возьмите pickle версию файла из предыдущей задачи.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.'''

__all__ = ['convert']

import pickle
import csv

def convert(f_pickle, f_csv):
    with(open(f_pickle, 'rb') as f_pi,
         open(f_csv, 'w', encoding='utf-8', newline='') as f_c):
        dct = pickle.load(f_pi)
        new_csv = csv.DictWriter(f_c, fieldnames=['id', 'level', 'name'], dialect='excel-tab',
                                 quoting=csv.QUOTE_ALL)
        new_csv.writeheader()
        new_csv.writerows(dct)


if __name__ == '__main__':
    convert('user.pickle', 'file.csv')