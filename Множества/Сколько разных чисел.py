# Вашей программе будут поступать на вход N списков, содержащих целые числа
# Для каждого введенного списка определите, сколько в нем встречается различных чисел.
# Входные данные
# Сперва поступает натуральное число N - количество списков
# В следующих N строк вводятся значения каждого списка, разделенные через пробел
# Выходные данные
# Вывести на отдельной строке количество различных чисел каждого
# введенного списка в том же порядке, в котором вводились списки
# Sample Input 1:
# 2
# 1 2 3 2 1
# 2 2 2 2 2 2
# Sample Output 1:
#
# 3
# 1
print(*[len(set(list(map(int, input().split())))) for _ in range(int(input()))],sep="\n")


