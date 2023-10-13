# В вашем распоряжении имеется вложенный список people,
# в котором хранятся имена и телефоны.
# Ваша задача создать словарь при помощи генератора словарей,
# в котором в качестве ключей будут храниться номера телефонов,
# а значениями будут имена владельцев.
# Обязательно сохраните этот словарь в переменной phone_book.
# Выводить ничего не нужно, только правильно заполните словарь
# в переменной phone_book

people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]
phone_book = {people[i][1]:people[i][0] for i in range(len(people))}
for i,j in phone_book.items():
    print(i,j)
#phone_book = { value: key for key, value in people}