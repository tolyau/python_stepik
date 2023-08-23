a = []
n,m = map(int,(input().split()))
a = [list(map(int, input().split())) for i in range(n)]
max_sc = 0
ms = 0
mi = 0
for i in range(n):
    max_try = 0
    s = 0
    for j in range(m):
        s+=a[i][j]
        if a[i][j]>max_try:
            max_try = a[i][j]

    if max_try>max_sc:
        max_sc = max_try
        ms = s
        mi = i
    elif max_try == max_sc and s>ms:
        max_sc = max_try
        ms = s
        mi = i
print(mi)

