s = input()
q = list(input())
leng = len(q)

for i in range(leng):
    if q[i]=='L':
        s = s[1:]+s[0]
    else:
        s = s[-1]+s[:-1]
print(s)