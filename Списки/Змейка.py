n = [int(s) for s in input().split()]  # считываем входные данные
l = []  # создаем пустой список

# создаем цикл для создания строк поочередно, в строках каждый элемент должен увеличиваться, если строка нечетная ее просто переворачиваем методом reverse и добавляем в наш лист!

for i in range(n[0]):
    row = [j for j in range(i * n[1], (i + 1) * n[1])]
    if i % 2 != 0:
        row.reverse()
    l.append(row)

# Выводим массив l
for row in l:
    print(*row)
