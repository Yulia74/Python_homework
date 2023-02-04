"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
не превосходящие числа N.
10 -> 0 1 2 3
"""

number = int(input('Введите число '))
search = 1
power = -1
while search <= number:
    search *= 2
    power += 1
    print(power, end=' ')
print('\n')