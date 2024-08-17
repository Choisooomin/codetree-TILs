arr = [input() for _ in range(10)]
n = input()
cnt = 0

for i in range(10):
    leng = len(arr[i])
    if arr[i][leng-1] == n:
        print(arr[i])
        cnt+=1
if cnt == 0:
    print('None')