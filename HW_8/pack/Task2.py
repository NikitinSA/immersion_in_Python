'''Прочитайте созданный в прошлом задании csv файл без использования
csv.DictReader. Распечатайте его как pickle строку.'''

__all__ = ['reader_file']

import csv
import pickle


def reader_file(csv_f):
    with open(csv_f, 'r', newline='') as f_c:
        csv_r = csv.reader(f_c, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        data = []
        keys = []
        for i, item in enumerate(csv_r):
            dct = {}
            if i == 0:
                keys = item
            else:
                for j, elem in enumerate(item):
                    dct[keys[j]] = elem
            if len(dct) != 0:
                data.append(dct)
        res = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')


if __name__ == '__main__':
    reader_file('file.csv')