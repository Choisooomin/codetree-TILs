a,b = tuple(map(int,input().split()))
c = a+b
c = str(c)
cnt = 0

for elem in c:
    if elem == '1':
        cnt+=1
print(cnt)