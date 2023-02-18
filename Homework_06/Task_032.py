'''
Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

Ввод:
[-5,9,0,3,-1,-2,1,4,-2,1-,2,0,-9,8,10,-9,0,-5,-5,7]
5
15
Вывод: [1,9,13,14,19]
'''

import random

n = int(input('Введите количество элементов массива: '))
list = []
for i in range(n):
    list.append(random.randint(-10, 10))
print(list)

min_num = int(input('Введите минимальный элемент диапазона: '))
max_num = int(input('Введите максимальный элемент диапазона: '))
list_new=[]
for i in range(len(list)):
    if min_num <= list[i] <= max_num:
        list_new.append(i)
print(list_new)


# строки 23-26 можно заменить (вариант решения без создания нового массива)

# for i in range(len(list)):
#     if min_num <= list[i] <= max_num:
#         print(i, end=' ')
# print('\n')