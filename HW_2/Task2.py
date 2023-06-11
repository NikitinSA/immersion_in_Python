'''Напишите программу, которая принимает две строки вида “a/b” - дробь с 
числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions.'''

from fractions import Fraction

fraction_1, fraction_2 = input('Введите первую дробь в формате "a/b": '), \
    input('Введите первую дробь в формате "a/b": ')

numerator_1 = ''
denominator_1 = ''
numerator_2 = ''
denominator_2 = ''

num_1, den_1 = map(int, fraction_1.split('/'))
num_2, den_2 = map(int, fraction_2.split('/'))

if denominator_1 == denominator_2:
    print(f'{num_1 + num_2}/{den_1}')
    print(f'{num_1 * num_2}/{den_1 * den_2}')
else:
    print(f'{num_1 * den_2 + num_2 * den_1}/{den_1 * den_2}')
    print(f'{num_1 * num_2}/{den_1 * den_2}')
    
print(Fraction(fraction_1) + Fraction(fraction_2))
print(Fraction(fraction_1) * Fraction(fraction_2))