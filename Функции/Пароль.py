# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
#
# Сложным паролем будет считаться комбинация символов, в которой :
#
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"
def check_password(password):
    f = False
    f1 = False
    f2 = False
    F3 = False
    if len(password) >= 10:
        f2 = True

    k = 0
    for i in password:
        if i.isdigit():
            k += 1
    if k >= 3:
        f3 = True
    for i in password:
        if i.isupper():
            f = True
    for i in password:
        if i in "!@#$%*":
            f1 = True
    if f and f1 and f2 and f3:
        print("Perfect password")
    else:
        print("Easy peasy")
check_password(input())



