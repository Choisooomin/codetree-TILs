n = int(input())
arr = [[1 for _ in range(n)]for _ in range(n)]

for i in range(n):
    for j in range(1,i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for row in range(n):
    for elem in range(row+1):
        print(arr[row][elem],end=' ')
    print()