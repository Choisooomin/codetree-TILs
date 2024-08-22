a,b = tuple(input().split())
A,B = ord(a), ord(b)

if A>B:
    c = A-B
else:
    c = B-A 
print(A+B,c)