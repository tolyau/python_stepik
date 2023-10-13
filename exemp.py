# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
import math

# day_distance = int(input("Введите расстояние в день: "))
# distance = int(input("Введите расстояние: "))
# days = distance//day_distance + (distance%day_distance > 0)
# print(days)
# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES
# year = int(input("Введите год: "))
# if year % 4 ==  0 and year % 100 != 0 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")

n = 24

# Введите ваше решение ниже

# P = S = (n//3)//2
# K = n - P*2
# print(f'{P} {K} {S}')
def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n+1) if primes[i]]

def prime_factors(n):
    factors = []
    primes = sieve_of_eratosthenes(n)
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors
print(prime_factors(3804025))