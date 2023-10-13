# Инициалы
# Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# middlename– отчество человека;
# а затем выводит на печать фамилию и инициалы в определенном формате
# (первая буква фамилии должна стать заглавной, все остальные строчные;
# в имени и отчестве остаются только по одной букве в верхнем регистре).
# Ваша задача дописать только тело функции print_initials
#
# Sample Input 1:
#
# Мария
# Иванова
# Филлиповна
# Sample Output 1:
#
# Иванова М.Ф.


# объявление функции
def print_initials(name, surname, middlename):
    return f'{surname.title()} {name.title()[0]}.{middlename.title()[0]}.'

# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print(print_initials(name, surname, middlename))
print(sum(6, 3))