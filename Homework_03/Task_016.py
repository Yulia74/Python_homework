"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

Input: 
5
1 2 3 4 5
3

Output: -> 1
"""

list = []
n = int(input("Введите количетсво элементов в массиве: "))
for i in range(1,n+1):
    list.append(i)
print(*list)
x = int(input("Введите число x: "))
count = 0
for i in range(len(list)):
    if list[i]==x:
        count+=1
print(f'число x встречается {count} раз(а)')