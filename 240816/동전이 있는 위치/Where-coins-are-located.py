n,m = tuple(map(int,input().split()))
arr = [[0 for _ in range(n+1)]for _ in range(n+1)]

for i in range(m):
    r,c = tuple(map(int,input().split()))
    arr[r][c] = 1

for row in range(1,n+1):
    for elem in range(1,n+1):
        print(arr[row][elem],end=' ')
    print()