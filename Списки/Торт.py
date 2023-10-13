a,b = map(int,input().split())
tort =[]
k=0


for i in range(a):
    tort.append(input())
mas = [[False]*b for i in range(a)]

for i in range(a):
    if 'S' not in tort[i]:
        for j in range(b):
            mas[i][j]=True
for j in range(b):
    is_f= False
    for i in range(a):
        if tort[i][j]=='S':
            is_f=True
            break
    if not is_f:
        for i in range(a):
            mas[i][j] = True
for row in mas:
    k+=row.count(True)


print(k)