def first_unique_char(s):
    for i in s:
        if s.count(i) == 1:
            s.index(i)
            

    return -1


s = input()
print(first_unique_char(s))
