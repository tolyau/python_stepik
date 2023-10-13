# Перед вами имеется словарь sweet
#
# Ваша задача:
#
# создать строковый ключ weight с целым значением 230
# создать строковый ключ have_topping c булевым значением True
# изменить значение ключа name на строку SuperCake
# изменить значение ключа calories на целое число 350
# В качестве ответа распечатайте в конце словарь sweet

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# sweet['weight'] = 230
# sweet['have_topping'] = True
# sweet['name'] = 'SuperCake'
# sweet['calories'] = 350
# print(sweet)

# На вход программе поступает целое число n. Вам необходимо создать словарь,
# который будет включать в себя ключи от 1 до n, а значениями соответствующего ключа
# будет значение ключа в квадрате.
# В качестве ответа выведите полученный словарь
# n = int(input())
# slov = {}
# for i in  range(1,n+1):
#     slov.setdefault(i,i*i)
# print(slov)

# from string import ascii_lowercase
# alphabet = {}
#
# for i in range(len(ascii_lowercase)):
#
#     alphabet.setdefault(ascii_lowercase[i],i+1)
#
# print(alphabet)


# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
# keys = list(account)
# print(keys)


# a = {1: "one", 2: "two"}
# b = {2: "dva", 3: "three"}
# c = {3: "tri", 2: "два"}
#
# result = c | a | b
# print(result)

# d1 = {'India': 'Delhi',
#       'Canada': 'Ottawa',
#       'United States': 'Washington D. C.'}
#
# d2 = {'France': 'Paris',
#       'Malaysia': 'Kuala Lumpur'}
# print(capitals := (d1 | d2))

d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}

d2.update(d1)
print(d2)