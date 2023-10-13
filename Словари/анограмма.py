s = input().lower()
a = input().lower()
clov = {}
cl = {}
for klu in s:
    if klu.isalpha():
        clov[klu] = clov.get(klu,0)+1
for klu in a:
    if klu.isalpha():
        cl[klu] = cl.get(klu,0)+1
if cl == clov:
    print("YES")
else:
    print("NO")


