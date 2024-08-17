a,b = tuple(input().split())
arra = list(a)
arrb = list(b)
arrb[0] = arra[0]
arrb[1] = arra[1]

b = ''.join(arrb)
print(b)