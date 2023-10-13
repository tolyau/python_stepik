# Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.
#
# Входные данные
# Входная строка может содержать цифры, пробелы и латинские буквы.
#
# Выходные данные
# Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.
#
# Sample Input 1:
#
# abc12cd34ef35
# Sample Output 1:
#
# 3
new_set = set()
fraz = input()
spisok=[]
spisok2=[]
for i in fraz:
    if i.isdigit() :
        spisok.append(int(i))
for i in spisok:
    if i not in new_set:
        new_set.add(i)
    else:
        spisok2.append(i)
if len(spisok2)==0:
        print('NO')
else:
    print(*set(sorted(spisok2)))