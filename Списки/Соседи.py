n, m = map(int,input().split())


mas = [(list(map(int, input().split()))) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        mas[i][j] = mas[i][j-1] + mas[i-1][j]

for i in range(0, n):
    for j in range(0, m):
        print(mas[i][j], end=" ")
    print()