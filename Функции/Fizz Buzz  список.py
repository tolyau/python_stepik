# Fizz Buzz  список
# Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число
# n - размер списка. Функция generate_fizz_buzz_list должна
#
# обойти числа от 1 до n включительно и для каждого такого числа выполнить
# последовательно проверки с пункта 2 по пункт 5
# Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz
# Если число кратно трем, то в список заносим строку Fizz
# Если число кратно пяти, то в список заносим строку Buzz
# Если число не кратно ни трем ни пяти, то в список заносим само это число
# В итоге функция generate_fizz_buzz_list должна вернуть сформированный список
# из n элементов. Ниже показаны примеры вызова:
#
# generate_fizz_buzz_list(3)  => [1, 2, 'Fizz']
# generate_fizz_buzz_list(7)  => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7]
# generate_fizz_buzz_list(15) => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']


def generate_fizz_buzz_list(n):
    new_list = []
    for i in range(1,n+1):
        if i %3==0 and i % 5 == 0:
            new_list.append('FizzBuzz')
        elif i%3==0:
            new_list.append('Fizz')
        elif i%5==0:
            new_list.append('Buzz')
        else:
            new_list.append(i)
    return new_list
n = int(input())
print(generate_fizz_buzz_list(n))