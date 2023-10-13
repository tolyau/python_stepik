# Ваша программа получает на вход последовательность фраз, указанных через запятую.
# Для каждой фразы выведите слово ДА (в отдельной строке),
# если эта фраза ранее встречалось в последовательности или НЕТ, если не встречалось.
# Символы во фразах нужно рассматривать без учета регистра, это значит что фраза Hasta la vista BAby
# эквивалента фразе hasta La Vista baby
#
# Sample Input 1:
#
# Hello world,hi dude,hello world,qwerty
# Sample Output 1:
#
# НЕТ
# НЕТ
# ДА
# НЕТ
# new_set = set()
# fraz = input().lower().split(',')
# for i in fraz:
#     if i in new_set:
#         print('ДА')
#     else:
#         print("НЕТ")
#     new_set.add(i)
#
#
# print(fraz,new_set)
set1 = set(list(map(int,input().split())))
set2 = set(list(map(int,input().split())))
set3 =sorted(list(set1-set2))

print(*set3)
