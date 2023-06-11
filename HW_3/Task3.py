'''Создайте словарь со списком вещей для похода в качестве ключа и их 
массой в качестве значения. Определите какие вещи влезут в рюкзак 
передав его максимальную грузоподъёмность. Достаточно вернуть один 
допустимый вариант.'''

things = {'Спички': 1, 'Кружка': 2, 'Палатка': 10, 'Рация': 5, 'Запасная обувь': 3}
load_capacity = int(input('Введите максимальную грузоподъемность рюкзака: '))
packaging_option = []

for key, value in things.items():
    if value <= load_capacity:
        load_capacity -= value
        packaging_option.append(key)

print(packaging_option)