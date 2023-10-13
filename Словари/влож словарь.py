a = list(map(int,input().split()))
b = {a[-2]:a[-1]}

for i in range(-3,-len(a)-1,-1):
    b = {a[i]:b}
print(b)