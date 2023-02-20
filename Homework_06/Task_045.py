'''
Два различных натуральных числа n и m называются дружественными, если сумма делителей
числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 –
дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое
из которых не превосходит k. Программа получает на вход одно натуральное число k,
не превосходящее 10^5. Программа должна вывести все пары дружественных чисел, каждое из
которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

Ввод: 300

Вывод: 220 284


k = int(input('Введите число k, не превышающее 10^5: '))

for i in range(1, k):
    m = 0
    n = 0
    for x in range(1, i): 
        if i % x == 0:
            m += x
    for j in range(1, m):
        if m % j == 0:
            n += j
    if i == n and i != m and i == min(i, m):
        print(i, m)

2 вариант решения задачи

n = int(input('Введите число n, не превышающее 10^5: '))

def sum_friendly(n):
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s

for i in range(1, n):
    j = sum_friendly(i)
    if i < j <= n and i == sum_friendly(j):
        print(i, j)

3 вариант решения задачи
'''
import time           # добавляем проверку на длительность выполенения кода

n = int(input())

start = time.time()   # засекаем время на выполнение

list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
            list_1.append(tuple([i, summa]))

for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i])

end = time.time()
print(end-start)
