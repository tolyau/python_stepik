n,m = map(int,input().split())
triangle =[list(map(int, input().split())) for i in range(n)]

for i in range(-2, -n-1,-1):
    for j in range(-2, -m-1,-1):
        triangle[i][j] = triangle[i][j+1] + triangle[i+1][j]

for i in range(n):
    for j in range(m):
        print(triangle[i][j], end=" ")
    print()