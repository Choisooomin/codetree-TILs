n,A = input().split()
n = int(n)
cnt = 0

for _ in range(n):
    elem = input()
    if A==elem:
        cnt+=1
print(cnt)