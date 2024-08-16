n = int(input())
arr = [[0for _ in range(n)] for _ in range(n)]
num = 1

for i in range(n-1, -1, -1):
    if (n - i) % 2 == 1:
        # 홀수 번째 열은 아래에서 위로 채우기
        for j in range(n-1, -1, -1):
            arr[j][i] = num
            num += 1
    else:
        # 짝수 번째 열은 위에서 아래로 채우기
        for j in range(n):
            arr[j][i] = num
            num += 1


for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()