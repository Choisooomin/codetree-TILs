A = input()
leng = len(A)

for i in range(leng-1,-1,-1):
    if i%2!=0:
        print(A[i],end='')