n = int(input())
cnt = 0
len_all = 0

arr = [input() for _ in range(n)]


for i in range(n):
    len_all += len(arr[i])
    if arr[i][0] == 'a':
        cnt+=1
        
print(len_all, cnt)