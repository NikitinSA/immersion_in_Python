'''Напишите функцию принимающую на вход только ключевые параметры и возвращающую 
словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.'''


def dicts(**kvargs):
    Garage = dict()
    for k, v in kvargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        Garage[v] = k
    return Garage


print(dicts(car='BMW', drivers={'Anna': 5, 'Elena': 2}, numbers=[
      'x929em', 'e125pa', 'a777aa']))
