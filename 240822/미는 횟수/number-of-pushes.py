A = input()
B = input()
n = 0
leng = len(A)

for i in range(leng):
    if A == B:
        break
    A = A[-1:] + A[:-1]
    n+=1
if A != B:
    n = -1

print(n)