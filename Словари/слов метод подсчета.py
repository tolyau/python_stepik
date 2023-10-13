s = input().lower()
clov = {}
for klu in s:
    if klu.isalpha():
        clov[klu] = clov.get(klu,0)+1
print(clov)

