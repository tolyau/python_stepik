n = [int(s) for s in input().split()]  # считываем входные данные
l = []  # создаем пустой список
pix =[]
for i in range(n[0]):
    pix.append(input().split())


for i in range(n[0]):
    for j in range(n[1]):
        if pix[i][j]=='C' or pix[i][j]=='M' or pix[i][j]=='Y':
            l.append(pix[i][j])
if len(l)>0:
    print('#Color')
else:
    print('#Black&White')

