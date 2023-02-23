'''
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля).
Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.

Ввод: 
print_operation_table(lambda x, y: x * y)

Вывод:
1  2  3   4   5   6
2  4  6   8   10  12
3  6  9   12  15  18
4  8  12  16  20  24
5 10  15  20  25  30
6 12  18  24  30  36 


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        table=[]
        for j in range(1, num_columns +1):
            table.append(str(operation(i,j)))          # str - т.к. список строк(многомерный массив)
        print('\t'.join(table))                        # .join обратная split() список превращает в строку 
                                                       # '\t'табуляция
        
print_operation_table(lambda x, y: x * y)  


2 вариант решения задачи
'''
def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print('ОЩИБКА! Размерности таблицы должны быть больше 2!')
    else:                                                                # '  ' разделитель между элементами
        print('\t'.join([str(i) for i in range(1, num_columns + 1)])) # первая строка просто заполняется 1,2,3,4,5,6
        for i in range(2, num_rows + 1):
            print(i, end = '\t')                      # print(i, end = '\t') означает, что следующий i будет через 'таб'
            for j in range(2, num_columns + 1):
                print(operation(i, j), end = '\t')
            print()                                   # перенос строки после каждого оборота цикла (40 строка)

print_operation_table(lambda x, y: x * y)

