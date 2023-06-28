# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

__all__ = ['rename']

import os

def rename(new_name: str, extension_old: str, extension_new: str, dir_name: str):
    dir_list = os.listdir(dir_name)
    count = 1
    for file in dir_list:
        file_extension = file.split('.')[1]
        if file_extension == extension_old:
            file_name = os.path.join(dir_name, f'{file.split(".")[0]}_{new_name}_{count}.{extension_new}')
            old_name = os.path.join(dir_name, file)
            os.rename(old_name, file_name)
            count += 1


if __name__ == '__main__':
    rename('test', 'docx', 'txt', 'D:\Geek Brains\погружение в Python\immersion_in_python\HW_7\Doc')