#
# Заполнение матрицы
# Ваша задача сформировать квадратную матрицу размером NxN, в которой используется следующее заполнение:
#
# все элементы, находящиеся выше главной диагонали, заполняются значением A;
# все элементы, находящиеся ниже главной диагонали, заполняются значением B;
# все элементы, находящиеся на главной диагонали, заполняются значением C.
# В качестве ответа, выведите на экран полученную матрицу
#
# Входные данные
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в матрицы, а затем на новой строке три целых числа  A, B и C. Данные числа используются для заполнения
#
# Выходные данные
# Заполните и распечатайте матрицу
#
# Sample Input 1:
#
# 3
# 1 0 3
# Sample Output 1:
#
# 3 1 1
# 0 3 1
# 0 0 3

n = int(input())
a,b,c = map(int, input().split())

for i in range(n):
    for j in range(n):
        if i == j:
            print(c, end=' ')

        elif i<j:
            print(a, end=' ')

        else:
            print(b, end=' ')
    print()

