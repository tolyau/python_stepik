# s = input()
# s1 = set()
# for i in s:
#     if i not in s1:
#         print(i,end='')
#     s1.add(i)


# k = 7
# a =[]
#
# for i in range(77):
#     a.append(k)
#     k=k*10+7
# my_frozen = frozenset(a)
# print(a)


my_frozen = frozenset([int('7' * i) for i in range(1, 78)])
print(my_frozen)