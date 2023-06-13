'''Дан список повторяющихся элементов. Вернуть список с дублирующимися 
элементами. В результирующем списке не должно быть дубликатов.'''

my_list = [1, 2, 3, 4, 4, 4, 5, 6, 2, 1, 6, 8, 9, 10]
list_without_repetitions = []

for i in my_list:
    if i not in list_without_repetitions and my_list.count(i) > 1:
         list_without_repetitions.append(i)

print(my_list, list_without_repetitions, sep='\n')