'''Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии'''

names = ['Дима', 'Миша', 'Марина']
salary = [20000, 40000, 60000]
prizes = ['10.15%', '20.00%', '30.65%']


def salary_gen(names: list[str], salary: list[int], prizes: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in prizes))}.items()


print(*(salary_gen(names, salary, prizes)))
